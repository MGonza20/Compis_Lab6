
from Parser import Parser
import sys

table = {0: {'(': ['s4'], 'id': ['s5'], 'E': ['1'], 'T': ['2'], 'F': ['3']}, 1: {'+': ['s7'], '*': ['s8'], '$': ['acc']}, 2: {'*': ['s11', 'r3'], ')': ['r3'], '+': ['r3'], '$': ['r3']}, 3: {'+': ['r5'], ')': ['r5'], '*': ['r5'], '$': ['r5']}, 4: {'(': ['s4'], 'id': ['s5'], 'E': ['6'], 'T': ['2'], 'F': ['3']}, 5: {'+': ['r7', 'r7'], '*': ['r7', 'r7'], ')': ['r7', 'r7'], '$': ['r7', 'r7']}, 6: {'+': ['s7'], '*': ['s8'], ')': ['s9']}, 7: {'(': ['s4'], 'id': ['s5'], 'T': ['13'], 'F': ['3']}, 8: {'(': ['s4'], 'id': ['s5'], 'T': ['10'], 'F': ['3']}, 9: {'+': ['r6'], '*': ['r6'], ')': ['r6'], '$': ['r6']}, 10: {'*': ['s11', 'r2'], ')': ['r2'], '+': ['r2'], '$': ['r2']}, 11: {'(': ['s4'], 'id': ['s5'], 'F': ['12']}, 12: {'+': ['r4'], ')': ['r4'], '*': ['r4'], '$': ['r4']}, 13: {'*': ['s11', 'r1'], ')': ['r1'], '+': ['r1'], '$': ['r1']}}
parser = Parser("sara_compis1_tools/slr-fatal-err.yalp")
parser.set_values()

class GeneratedParser:
	def yalp_error(self):
		return []

	def eval_table(self):
		return parser.eval_table(table)

	def eval_chain(self, table, chain):
		parser.eval_string(table, chain)

	def return_tokens(self):
		return ['id', '+', '(', ')', '*', 'espacioEnBlanco']

	def return_table(self):
		return table

