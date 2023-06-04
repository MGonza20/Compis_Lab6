
from Parser import Parser
import sys

table = {0: {'(': ['s4'], 'id': ['s5'], 'E': ['1'], 'T': ['2'], 'F': ['3']}, 1: {'+': ['s7'], '$': ['acc']}, 2: {'*': ['s10'], ')': ['r2'], '+': ['r2'], '$': ['r2']}, 3: {'*': ['r4'], '$': ['r4'], '+': ['r4'], ')': ['r4']}, 4: {'(': ['s4'], 'id': ['s5'], 'E': ['6'], 'T': ['2'], 'F': ['3']}, 5: {')': ['r6'], '$': ['r6'], '*': ['r6'], '+': ['r6']}, 6: {'+': ['s7'], ')': ['s8']}, 7: {'(': ['s4'], 'id': ['s5'], 'T': ['9'], 'F': ['3']}, 8: {')': ['r5'], '$': ['r5'], '*': ['r5'], '+': ['r5']}, 9: {'*': ['s10'], ')': ['r1'], '+': ['r1'], '$': ['r1']}, 10: {'(': ['s4'], 'id': ['s5'], 'F': ['11']}, 11: {'*': ['r3'], '$': ['r3'], '+': ['r3'], ')': ['r3']}}
parser = Parser("sara_compis1_tools/slr-2.yalp")
parser.set_values()

class GeneratedParser:
	def yalp_error(self):
		return [('Error (Sintactico) en la linea 3:\nError en comentario', 3), ('Error (Sintactico) en la linea 15:\nError en comentario', 15), ('Error (Sintactico) en la linea 13:\nNo es valido declarar tokens luego del separador %%', 13), ('Error (Sintactico) en la linea 17:\nEl token + no esta declarado', 17)]

	def eval_table(self):
		return parser.eval_table(table)

	def eval_chain(table, chain):
		parser.eval_string(table, chain)

	def return_tokens(self):
		return ['id', '(', ')', '*', 'espacioEnBlanco', 'espacioEnBlanco']

