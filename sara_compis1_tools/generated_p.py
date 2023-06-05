
from Parser import Parser
import sys

table = {0: {'printStatement': ['s5'], '(': ['s8'], 'id': ['s9'], 'S': ['1'], 'EP': ['2'], 'E': ['3'], 'P': ['4'], 'T': ['6'], 'F': ['7']}, 1: {'printStatement': ['s5'], '(': ['s8'], 'id': ['s9'], '$': ['acc'], 'E': ['3'], 'P': ['4'], 'T': ['6'], 'F': ['7'], 'EP': ['21']}, 2: {'$': ['r2'], '(': ['r2'], 'id': ['r2'], 'printStatement': ['r2']}, 3: {'+': ['s11'], '$': ['r3'], 'id': ['r3'], '(': ['r3'], 'printStatement': ['r3']}, 4: {'$': ['r4'], 'id': ['r4'], '(': ['r4'], 'printStatement': ['r4']}, 5: {'(': ['s16']}, 6: {'*': ['s14'], '$': ['r6'], '+': ['r6'], ')': ['r6'], '(': ['r6'], 'id': ['r6'], 'printStatement': ['r6']}, 7: {'$': ['r8'], '+': ['r8'], ')': ['r8'], '(': ['r8'], 'id': ['r8'], 'printStatement': ['r8'], '*': ['r8']}, 8: {'(': ['s8'], 'id': ['s9'], 'E': ['10'], 'T': ['6'], 'F': ['7']}, 9: {'$': ['r10'], '(': ['r10'], 'id': ['r10'], '+': ['r10'], ')': ['r10'], 'printStatement': ['r10'], '*': ['r10']}, 10: {'+': ['s11'], ')': ['s12']}, 11: {'(': ['s8'], 'id': ['s9'], 'T': ['13'], 'F': ['7']}, 12: {'$': ['r9'], '(': ['r9'], 'id': ['r9'], '+': ['r9'], ')': ['r9'], 'printStatement': ['r9'], '*': ['r9']}, 13: {'*': ['s14'], '$': ['r5'], '+': ['r5'], ')': ['r5'], '(': ['r5'], 'id': ['r5'], 'printStatement': ['r5']}, 14: {'(': ['s8'], 'id': ['s9'], 'F': ['15']}, 15: {'$': ['r7'], '+': ['r7'], ')': ['r7'], '(': ['r7'], 'id': ['r7'], 'printStatement': ['r7'], '*': ['r7']}, 16: {'cadena': ['s17'], 'enteros': ['s18']}, 17: {')': ['s20']}, 18: {')': ['s19']}, 19: {'$': ['r12'], '(': ['r12'], 'id': ['r12'], 'printStatement': ['r12']}, 20: {'$': ['r11'], '(': ['r11'], 'id': ['r11'], 'printStatement': ['r11']}, 21: {'$': ['r1'], '(': ['r1'], 'id': ['r1'], 'printStatement': ['r1']}}
parser = Parser("slr-3-ok.yalp")
parser.set_values()

class GeneratedParser:
	def yalp_error(self):
		return []

	def eval_table(self):
		return parser.eval_table(table)

	def eval_chain(self, table, chain):
		parser.eval_string(table, chain)

	def return_tokens(self):
		return ['id', 'printStatement', 'cadena', 'enteros', '+', '(', ')', '*', 'espacioEnBlanco']

	def return_table(self):
		return table

