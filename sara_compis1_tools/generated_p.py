
from Parser import Parser
import sys

table = {0: {'printStatement': ['s5'], '(': ['s8'], 'id': ['s9'], 'S': ['1'], 'EP': ['2'], 'E': ['3'], 'P': ['4'], 'T': ['6'], 'F': ['7']}, 1: {'printStatement': ['s5'], '(': ['s8'], 'id': ['s9'], '$': ['acc'], 'E': ['3'], 'P': ['4'], 'T': ['6'], 'F': ['7'], 'EP': ['21']}, 2: {'printStatement': ['r2'], '(': ['r2'], '$': ['r2'], 'id': ['r2']}, 3: {'+': ['s11'], '(': ['r3'], 'id': ['r3'], 'printStatement': ['r3'], '$': ['r3']}, 4: {'(': ['r4'], 'id': ['r4'], 'printStatement': ['r4'], '$': ['r4']}, 5: {'(': ['s16']}, 6: {'*': ['s14'], 'printStatement': ['r6'], '(': ['r6'], '$': ['r6'], '+': ['r6'], 'id': ['r6'], ')': ['r6']}, 7: {'printStatement': ['r8'], '(': ['r8'], '*': ['r8'], '+': ['r8'], '$': ['r8'], 'id': ['r8'], ')': ['r8']}, 8: {'(': ['s8'], 'id': ['s9'], 'E': ['10'], 'T': ['6'], 'F': ['7']}, 9: {'(': ['r10'], '*': ['r10'], '+': ['r10'], 'id': ['r10'], ')': ['r10'], 'printStatement': ['r10'], '$': ['r10']}, 10: {'+': ['s11'], ')': ['s12']}, 11: {'(': ['s8'], 'id': ['s9'], 'T': ['13'], 'F': ['7']}, 12: {'(': ['r9'], '*': ['r9'], '+': ['r9'], 'id': ['r9'], ')': ['r9'], 'printStatement': ['r9'], '$': ['r9']}, 13: {'*': ['s14'], 'printStatement': ['r5'], '(': ['r5'], '$': ['r5'], '+': ['r5'], 'id': ['r5'], ')': ['r5']}, 14: {'(': ['s8'], 'id': ['s9'], 'F': ['15']}, 15: {'printStatement': ['r7'], '(': ['r7'], '*': ['r7'], '+': ['r7'], '$': ['r7'], 'id': ['r7'], ')': ['r7']}, 16: {'cadena': ['s17'], 'enteros': ['s18']}, 17: {')': ['s20']}, 18: {')': ['s19']}, 19: {'id': ['r12'], '(': ['r12'], '$': ['r12'], 'printStatement': ['r12']}, 20: {'id': ['r11'], '(': ['r11'], '$': ['r11'], 'printStatement': ['r11']}, 21: {'printStatement': ['r1'], '(': ['r1'], '$': ['r1'], 'id': ['r1']}}
parser = Parser("slr-3.yalp")
parser.set_values()

class GeneratedParser:
	def yalp_error(self):
		return [('Error (Sintactico) en la linea 3:\nError en comentario', 3), ('Error (Sintactico) en la linea 18:\nError en comentario', 18), ('Error (Sintactico) en la linea 15:\nNo es valido declarar tokens luego del separador %%', 15), ('Error (Sintactico) en la linea 30:\nEl token + no esta declarado', 30)]

	def eval_table(self):
		return parser.eval_table(table)

	def eval_chain(self, table, chain):
		parser.eval_string(table, chain)

	def return_tokens(self):
		return ['id', 'printStatement', 'cadena', 'enteros', '(', ')', '*', 'espacioEnBlanco']

	def return_table(self):
		return table

