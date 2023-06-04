
import networkx as nx
from graphviz import Digraph


class ruleLine:
    def __init__(self, line_no, line):
        self.line_no = line_no
        self.line = line

class prod_obj:
    def __init__(self, name):
        self.name = name
        self.production = []

class group_i:
    def __init__(self):
        self.heart = []
        self.productions = []
        self.transitions = {}


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.tokens = []
        self.ignored_tokens = []
        self.productions = []
    
    def clean_comments(self, joined):
        for index, line in enumerate(joined):
            line_wo_comment = ''
            i = 0
            while i < len(line):
                if i < len(line) - 1 and line[i] == '/' and line[i + 1] == '*':
                    while i < len(line) - 1 and (line[i] != '*' or line[i + 1] != '/'):
                        i += 1
                    i += 2
                else:
                    line_wo_comment += line[i]
                    i += 1
            joined[index] = line_wo_comment
        return joined
    

    def analyze_yapar(self):
        lines = self.getLines(yapar=True)
        errors = [] 

        for index, line in enumerate(lines, start=1):
            if line.count('/*') != line.count('*/'):
                errors.append(('Error en la linea ' + str(index) + ':\nError en comentario', index))

        splits = [line.split(' ') for line in lines]
        splits = self.remove_spaces_list(splits)

        separator = [indx for indx, line in enumerate(splits) if line and line[0] == '%%']
        if separator:
            for i_line, line in enumerate(splits, start=1):
                if line and line[0] == '%token' and i_line > separator[0]:
                    errors.append(('Error en la linea ' + str(i_line) + ':\nNo es valido declarar tokens luego del separador %%', i_line))

        # self.set_values()
        non_terminals = self.get_non_terminal()

        for indx, line in enumerate(splits, start=1):
            if line[0] and line[0][-1] == ':':
                prod = prod_obj(line[0][:-1])

                while True:
                    prod, element, list_ = self.process_elements(splits[indx], prod, multiple_r=True)
                    if element[-1] == ';':
                        break
                    else:
                        indx += 1
                        for element in list_:
                            if element not in non_terminals and element not in self.tokens and element not in ['|', 'ε']:
                                errors.append(('Error en la linea ' + str(indx) + ':\nEl token ' + element + ' no esta declarado', indx))
                indx += 1

        return errors




    def getLines(self, yapar=False):
        f = open(self.filename, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        
        lines_with_n = [n[:-1] if n[-1] == '\n' else n for n in lines]
        check_comments = [lll.split(' ') for lll in lines_with_n]  
        joined = [' '.join(line) for line in check_comments]
        
        if not yapar:
            return self.clean_comments(joined)
        else:
            return joined
    

    def remove_spaces_list(self, lines):
        for line in lines:
            if not all(element == '' for element in line):
                while '' in line:
                    for element in line:
                        if element == '':
                            line.pop(line.index(element))
        return lines
    

    def process_elements(self, line, prod, multiple_r=False):
        list_ = []
        for element in line:
            if element == '|':
                if list_:
                    prod.productions.append(list_)
                list_ = []
            elif element[-1] == ';':
                if len(element) > 1:
                    list_.append(element[:-1])
                else:
                    if element and element != ';':
                        list_.append(element)
                if list_:
                    prod.productions.append(list_)
                break
            else:
                list_.append(element)

        if multiple_r:
            return prod, element, list_
        else:
            return prod
    
    
    def set_values(self):
        splits = [line.split(' ') for line in self.getLines()]
        splits = self.remove_spaces_list(splits)
        
        for indx, line in enumerate(splits, start=1):
            if line[0] == '%token':
                for token in line[1:]:
                    self.tokens.append(token)
            elif line[0] == 'IGNORE':
                for token in line[1:]:
                    if token in self.tokens:
                        ignored_token = self.tokens.pop(self.tokens.index(token))
                        self.ignored_tokens.append(ignored_token)

            elif line[0] and line[0][-1] == ':':
                prod = prod_obj(line[0][:-1])

                if len(line) > 1:
                    prod = self.process_elements(line[1:], prod)
                    self.productions.append(prod)
                else:
                    while True:
                        prod, element, list_ = self.process_elements(splits[indx], prod, multiple_r=True)
                        if element[-1] == ';':
                            break
                        else:
                            prod.production.append(list_)
                            indx += 1

                    self.productions.append(prod)
                    indx += 1

    def return_tokens(self):
        self.set_values()
        return self.tokens + self.ignored_tokens

    def process_element_productions(self, element, checked, to_do, new_group):
        
        all_productions = self.productions.copy()
        element_productions = [prod for prod in all_productions if prod.name == element]
        if not element_productions:
            return

        element_production = element_productions[0]
        for production in element_production.production:

            first_element = production[0]
            if first_element not in checked:
                checked.append(first_element)
                to_do.append(first_element)

            new_production = ['•'] + production
            if new_production not in new_group.productions:
                new_prod_obj = prod_obj(element_production.name)
                new_prod_obj.production = new_production
                new_group.productions.append(new_prod_obj)


    def get_non_terminal(self):
        non_terminal = []
        for prod in self.productions:
            if prod.name not in non_terminal:
                non_terminal.append(prod.name)
        return non_terminal        


    def closure(self, heart_prductions):
        non_terminal_names = list(set(prod.name for prod in self.productions))

        new_group = group_i()
        for heart_production in heart_prductions:
            new_group.heart.append(heart_production)

        checked = []
        to_do = []

        for item in new_group.heart:
            dot_index = item.production.index('•')
            if dot_index +1 < len(item.production):
                element_after_dot = item.production[dot_index + 1]
                checked.append(element_after_dot)
                self.process_element_productions(element_after_dot, checked, to_do, new_group)

        while to_do:
            element = to_do.pop()
            if element in non_terminal_names:
                self.process_element_productions(element, checked, to_do, new_group)
        
        return new_group
    

    def go_to(self, group, element):
        new_group = group_i()
        all_productions = [prod for prod in group.productions] + [prod for prod in group.heart]

        for p in all_productions:
            dot_index = p.production.index('•')
            if dot_index + 1 < len(p.production) and p.production[dot_index + 1] == element:
                new_p = p.production.copy()
                new_p.pop(dot_index)
                new_p.insert(dot_index + 1, '•')
                new_prod_obj = prod_obj(p.name)
                new_prod_obj.production = new_p
                new_group.heart.append(new_prod_obj)
        
        res = self.closure(new_group.heart).productions
        new_group.productions =  res if res else []

        return new_group



    def get_group_transitions(self, group):
        transitions = []
        all_productions = [prod for prod in group.productions] + [prod for prod in group.heart]
        
        for p in all_productions:
            dot_index = p.production.index('•')
            if dot_index + 1 < len(p.production):
                element_after_dot = p.production[dot_index + 1]
                if element_after_dot not in transitions:
                    transitions.append(element_after_dot)
                # transitions.add(element_after_dot)

        return list(transitions)


    def same_heart(self, lista1, lista2):
        return len(lista1) == len(lista2) and all(item in lista2 for item in lista1)


    def repeated(self, obj, dict_repeated):
        c_list = []
        for els in obj:
            list_ = [els.name] + els.production
            c_list.append(list_)

        for key, value in dict_repeated.items():
            reps_values = [[v.name] + v.production for v in value]
            if self.same_heart(reps_values, c_list):
                return key
        return None
    

    def construct_automata(self):
        first_prod = self.productions[0]
        augmented_p = prod_obj(f"{first_prod.name}'")
        augmented_p.production = ['•', first_prod.name]

        groups = {}
        group_count = 0
        augmented_prod = self.closure([augmented_p])
        groups[group_count] = augmented_prod
        toDo = [group_count]

        dict_repeated = {}
        dict_repeated[group_count] = augmented_prod.heart
        
        while toDo:
            no = toDo.pop()
            transitions = self.get_group_transitions(groups[no])
            for t in transitions:
                if t != 'ε':
                    new_group = self.go_to(groups[no], t)
            
                    if new_group.heart:
                        existing_group_no = self.repeated(new_group.heart, dict_repeated)
                        
                        if not existing_group_no:
                            group_count += 1
                            groups[group_count] = new_group
                            dict_repeated[group_count] = new_group.heart
                            toDo.append(group_count)
                            groups[no].transitions[t] = group_count

                        else:
                            groups[no].transitions[t] = existing_group_no
                
        for no, new_group in groups.items():
            for h in new_group.heart:
                if h.name == augmented_p.name  and h.production[-1] == '•':
                    groups[no].transitions['$'] = 'aceptar'

        return groups
    

            
    def construct_slr_table(self, automata):
        table = {}
        all_prods = [[prod.name] + p for prod in self.productions for p in prod.production]
        non_terminal = self.get_non_terminal()

        for no, state in automata.items():
            table[no] = {}
            for transition, final_dest in state.transitions.items():
                
                # Assigning accept
                if transition == '$' and final_dest == 'aceptar':
                    table[no]['$'] = ['acc']

                # Assigning shift
                elif transition not in non_terminal:
                    if not table[no].get(transition):
                        table[no][transition] = []
                    table[no][transition].append(f's{final_dest}')

        for no, state in automata.items():
            # Assigning reduce
            for h in state.heart:
                if h.production[-1] == '•':
                    # Condition to not assign reduce to the augmented production
                    augmented_prod = f"{self.productions[0].name}'"
                    if h.name != f"{self.productions[0].name}'":

                        if h.name == self.productions[0].name:
                            follow_res = self.follow(h.name, init=True)
                        else:
                            follow_res = self.follow(h.name)

                        for f in follow_res:
                            no_dot = h.production.copy()
                            no_dot.pop()                 
                            complete_prod = [h.name] + no_dot         
                            if not table[no].get(f):
                                table[no][f] = []      
                            table[no][f].append(f'r{all_prods.index(complete_prod) +1}')

        # Assigning goto
        for no, state in automata.items():
            for transition, final_dest in state.transitions.items():
                if transition in non_terminal:
                    if not table[no].get(transition):
                        table[no][transition] = []
                    table[no][transition].append(f'{final_dest}')
                                
        return table
    

    def eval_string(self, table, input_str):

        stack = [0]
        all_prods = [[prod.name] + p for prod in self.productions for p in prod.production]
        
        while True:
            print(stack, input_str)
            action = table[stack[-1]][input_str[0]]

            if len(action) > 1:
                if action[0][0] == 'r' and action[1][0] == 's' or action[0][0] == 's' and action[1][0] == 'r':
                    raise Exception('Error: Reducion-Desplazamiento')
                elif action[0][0] == 'r' and action[1][0] == 'r':
                    raise Exception('Error: Reducion-Reduccion')

            else:
                action = action[0]
                # in case is a shift
                if action[0] == 's':
                    stack.append(int(action[1:]))
                    input_str = input_str[1:]
                
                # in case is a reduce
                elif action[0] == 'r':
                    prod = all_prods[int(action[1:]) - 1]
                    for _ in range(len(prod[1:])):
                        stack.pop()
                    stack.append(int(table[stack[-1]][prod[0]][0]))
                
                # in case the input string is accepted
                elif action == 'acc':
                    return 'Cadena aceptada'
                else:
                    stack.append(action)
                if not input_str:
                    return 'Cadena no aceptada'



                                     
    def draw_automata_p(self, automata):
        G = nx.MultiDiGraph()
        for no, state in automata.items():
            h_list = [(p.name, '→', ' '.join(p.production)) for p in state.heart]
            h_list = [' '.join(h) for h in h_list]
            h_list = '<BR/>'.join(h_list)
            p_list = [(p.name, '→', ' '.join(p.production)) for p in state.productions]
            p_list = [' '.join(p) for p in p_list]
            p_list = '<BR/>'.join(p_list)
            G.add_node(str(no), h_list=h_list, p_list=p_list)

            for transition, final_dest in state.transitions.items():
                G.add_node(str(final_dest))
                G.add_edge(str(no), str(final_dest), label=transition, dir='forward')

        dot = Digraph()
        dot.attr(rankdir='LR') 
        dot.attr(splines='polyline') 
        for u, v, data in G.edges(data=True):
            dot.edge(u, v, label=data['label'], dir=data['dir'])
        for node in G.nodes:
            if node == 'aceptar':
                dot.node(node, shape='none')
            else:
                attrs = G.nodes[node]
                dot.node(node, '''<
                <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                    <TR><TD>{0}</TD></TR>
                    <TR><TD BGCOLOR="lightgrey">{1}</TD></TR>  
                </TABLE>>'''.format(attrs['h_list'], attrs['p_list']), shape='none')
        dot.render('x/automata_xx', format='png')


    def first(self, element):
        non_terminal = list(set(prod.name for prod in self.productions))
        all_prods = [[prod.name] + p for prod in self.productions for p in prod.production]

        values = set()
        if element not in non_terminal:
            values.add(element)

        to_analyze = {p[1] for p in all_prods if len(p) > 1 and p[0] == element}
        done = set()

        while to_analyze:
            a = to_analyze.pop()
            if a not in non_terminal:
                values.add(a)
            else:
                done.add(a)
                for p in all_prods:
                    if len(p) > 1 and p[0] == a and p[1] not in done:
                        to_analyze.add(p[1])
        return values
    

    def all_first(self):
        non_terminal = list(set(prod.name for prod in self.productions))
        return {nt: self.first(nt) for nt in non_terminal}
    

    def follow(self, element, init=False, results=None):
        all_prods = [[prod.name] + p for prod in self.productions for p in prod.production]
        non_terminal = self.get_non_terminal()
        first = non_terminal[0]

        if not results:
            results = {nt: set() for nt in non_terminal}

        if element in results and results[element]:
            return results[element]

        element_indexes =  []
        for i, p in enumerate(all_prods):
            if element in p[1:]:
                element_indexes.append((i, p[1:].index(element)+1))

        if init:
            results[first].add('$')

        for no_list, pos in element_indexes:
            
            if pos+1 <= len(all_prods[no_list])-1:
                betha = all_prods[no_list][pos+1]
                betha_first = self.first(betha)
                betha_first.discard('ε')
                results[element] = results[element].union(betha_first)

            if pos == len(all_prods[no_list])-1:
                A = all_prods[no_list][0]
                follow_A = self.follow(A, init=True, results=results) \
                           if A == first else self.follow(A, results=results)
                if follow_A:
                    if 'ε' in follow_A:
                        follow_A.remove('ε')
                    results[element] = results[element].union(follow_A)

            if pos+1 <= len(all_prods[no_list])-1 and 'ε' in self.first(all_prods[no_list][pos+1]):
                A = all_prods[no_list][0]
                follow_A = self.follow(A, init=True, results=results) \
                           if A == first else self.follow(A, results=results)
                if follow_A:
                    follow_A.discard('ε')
                    results[element] = results[element].union(follow_A)
            
        return results[element]

        
    def all_follows(self):
        non_terminal = []
        for prod in self.productions:
            if prod.name not in non_terminal:
                non_terminal.append(prod.name)

        follows = {}
        for i, nt in enumerate(non_terminal):
            if i:
                follows[nt] = self.follow(nt)
            else:
                follows[nt] = self.follow(nt, init=True)

        return follows




                
        



if __name__ == "__main__":
    parser = Parser("sara_compis1_tools/slr-2-ok.yalp")
    parser.set_values()
    err = parser.analyze_yapar()
    wut = parser.construct_automata()
    table = parser.construct_slr_table(wut)
    tokens = parser.tokens + parser.ignored_tokens
    
    with open('sara_compis1_tools/generated_p.py', 'w', encoding="utf-8") as file:
        file.write('\nfrom Parser import Parser')
        file.write('\n\ntable = ' + str(table))

        file.write("\n\nclass Generated_parser:\n")
        file.write("\tdef return_tokens(self):\n")
        file.write("\t\treturn [")

        for indx, token in enumerate(tokens):
            if indx == len(tokens) - 1:
                file.write(f"'{token}'")
            else:
                file.write(f"'{token}',")
        file.write("]\n\n")

        file.write("\tdef analyze(self, yalp_file, input):\n")
        file.write("\t\tparser = Parser(yalp_file)\n")

        file.write("\t\tans = parser.eval_string(table, input)\n")




    # ans = parser.eval_string(table, ['id', '*', 'id', '+', 'id', '$'])
    # a = 1


