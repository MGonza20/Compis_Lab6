
import sys

from generated import Generated
from generated_p import GeneratedParser
from Parser import Parser
from lexEval import LexEval


g = Generated() 

p = GeneratedParser()
tokens_parser = p.return_tokens()
tokens_parser = set(tokens_parser)

tokens_scanner = set(g.return_tokens())

all_errors = []

# obtencion de tokens reconocidos o errores del scanner
res_parse = g.parse('sara_compis1_tools/con1_1_test')
lex_eval = LexEval('sara_compis1_tools/con1_1_test')
marker, content = lex_eval.get_recognized_tokens(res_parse)

if marker == 'err':
    content = sorted(content, key=lambda x: x[1])
    for err, indx in content:
        all_errors.append(err)
elif marker == 'tk':
    recognized_toks = content

# errores del analizador sintactico
errors = p.yalp_error()
errors = sorted(errors, key=lambda x: x[1])
for error_message, indx in errors:
    all_errors.append(error_message)

# Si los tokens no son iguales
if set(tokens_scanner) != set(tokens_parser):
    all_errors.insert(0, 'Error:\nLos tokens no son iguales en el scanner y el parser')

if all_errors:
    print()
    for error_message in all_errors:
        print(f'{error_message}\n')
else:    
    pass