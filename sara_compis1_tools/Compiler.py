
import sys

from generated import Generated
from Parser import Parser


# if len(sys.argv) < 2:
#     print('Por favor ingrese el archivo plano')
#     sys.exit(1)
# yal_file = sys.argv[1]


all_errors = []

g = Generated()  
res_parse = g.parse('sara_compis1_tools/con1_1_test')


tokens, errors = result_sim
if not errors:
    print('')
    for token in tokens:
        exec(token)
    else:
        print('\n')
        errors = self.sort_errors(errors)
        for error in errors:
            if error.position:
                print(f'Error en línea {error.line}: \n{error.error}, posición {error.position}\n')
            else:   
                print(f'Error en línea {error.line}: \n{error.error}\n')



tokens_scanner = set(g.return_tokens())

# p = Parser(yal_file)
# tokens_parser = set(p.return_tokens())


errors = p.analyze_yapar()
errors = sorted(errors, key=lambda x: x[1])
for error_message, indx in errors:
    all_errors.append(error_message)
if set(tokens_scanner) != set(tokens_parser):
    all_errors.insert(0, 'Error:\nLos tokens no son iguales en el scanner y el parser')


if all_errors:
    print()
    for error_message in all_errors:
        print(f'{error_message}\n')
else:    
    auto = p.construct_automata()
    p.draw_automata_p(auto)

    firsts = p.all_first()
    follows = p.all_follows()

    print('\nResultados de funcion primero:')
    for k, v in firsts.items():
        print(f'Primero({k}) = {v}')

    print('\nResultados de funcion siguiente:')
    for k, v in follows.items():
        print(f'Siguiente({k}) = {v}')
    print()
