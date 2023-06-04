
from Parser import Parser
import sys

table = {0: {'(': ['s4'], 'id': ['s5'], 'E': ['1'], 'T': ['2'], 'F': ['3']}, 1: {'+': ['s7'], '$': ['acc']}, 2: {'*': ['s10'], '$': ['r2'], '+': ['r2'], ')': ['r2']}, 3: {'+': ['r4'], '$': ['r4'], ')': ['r4'], '*': ['r4']}, 4: {'(': ['s4'], 'id': ['s5'], 'E': ['6'], 'T': ['2'], 'F': ['3']}, 5: {'+': ['r6'], ')': ['r6'], '*': ['r6'], '$': ['r6']}, 6: {'+': ['s7'], ')': ['s8']}, 7: {'(': ['s4'], 'id': ['s5'], 'T': ['9'], 'F': ['3']}, 8: {'+': ['r5'], ')': ['r5'], '*': ['r5'], '$': ['r5']}, 9: {'*': ['s10'], '$': ['r1'], '+': ['r1'], ')': ['r1']}, 10: {'(': ['s4'], 'id': ['s5'], 'F': ['11']}, 11: {'+': ['r3'], '$': ['r3'], ')': ['r3'], '*': ['r3']}}

if len(sys.argv) < 2:
	print("Por favor ingrese el archivo .yal")
	sys.exit(1)

parser = Parser(sys.argv[1])
parser.set_values()

err = []
if err:
	for e, indx in err:
		print(e)
else:
	errores = parser.eval_table(table)
	if errores:
		for error in errores:
			print(error)
	else:
		parser.eval_string(table, ['id', '*', 'id', '+', 'id', '$'])
