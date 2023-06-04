
import sys

from generated import Generated
from generated_p import Generated_parser


if len(sys.argv) < 2:
    print('Por favor ingrese el archivo plano')
    sys.exit(1)
yal_file = sys.argv[1]



g = Generated()
tokens_scanner = set(g.return_tokens())

p = Generated_parser(yal_file)
tokens_parser = set(p.return_tokens())


errors = p.analyze_yapar()
errors = sorted(errors, key=lambda x: x[1])
all_errors = []
for error_message, indx in errors:
    all_errors.append(error_message)
if set(tokens_scanner) != set(tokens_parser):
    all_errors.insert(0, 'Error:\nLos tokens no son iguales en el scanner y el parser')


if all_errors:
    print()
    for error_message in all_errors:
        print(f'{error_message}\n')
else:    
    pass