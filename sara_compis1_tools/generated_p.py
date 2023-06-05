
from Parser import Parser
import sys

table = {0: {'(': ['s6'], 'id': ['s7'], 'printStatement': ['s8'], 'S': ['1'], 'EP': ['2'], 'E': ['3'], 'P': ['4'], 'F': ['5'], 'T': ['9']}, 1: {'(': ['s6'], 'id': ['s7'], 'printStatement': ['s8'], '$': ['acc'], 'E': ['3'], 'P': ['4'], 'F': ['5'], 'T': ['9'], 'EP': ['22']}, 2: {'$': ['r2'], 'printStatement': ['r2'], '(': ['r2'], 'id': ['r2']}, 3: {'+': ['s19'], '$': ['r3'], '(': ['r3'], 'id': ['r3'], 'printStatement': ['r3']}, 4: {'$': ['r4'], '(': ['r4'], 'id': ['r4'], 'printStatement': ['r4']}, 5: {'$': ['r5', 'r9'], '(': ['r5', 'r9'], 'id': ['r5', 'r9'], 'printStatement': ['r5', 'r9'], ')': ['r9'], '*': ['r9'], '+': ['r9']}, 6: {'(': ['s6'], 'id': ['s7'], 'E': ['17'], 'T': ['9'], 'F': ['18']}, 7: {'$': ['r11'], ')': ['r11'], '*': ['r11'], '+': ['r11'], '(': ['r11'], 'id': ['r11'], 'printStatement': ['r11']}, 8: {'(': ['s12']}, 9: {'*': ['s10'], '$': ['r7'], '(': ['r7'], ')': ['r7'], 'id': ['r7'], 'printStatement': ['r7'], '+': ['r7']}, 10: {'(': ['s6'], 'id': ['s7'], 'F': ['11']}, 11: {'$': ['r8'], '(': ['r8'], ')': ['r8'], 'id': ['r8'], 'printStatement': ['r8'], '*': ['r8'], '+': ['r8']}, 12: {'cadena': ['s13'], 'enteros': ['s14']}, 13: {')': ['s16']}, 14: {')': ['s15']}, 15: {'$': ['r13'], 'printStatement': ['r13'], '(': ['r13'], 'id': ['r13']}, 16: {'$': ['r12'], 'printStatement': ['r12'], '(': ['r12'], 'id': ['r12']}, 17: {'+': ['s19'], ')': ['s20']}, 18: {'$': ['r9'], '(': ['r9'], ')': ['r9'], 'id': ['r9'], 'printStatement': ['r9'], '*': ['r9'], '+': ['r9']}, 19: {'(': ['s6'], 'id': ['s7'], 'E': ['21'], 'T': ['9'], 'F': ['18']}, 20: {'$': ['r10'], ')': ['r10'], '*': ['r10'], '+': ['r10'], '(': ['r10'], 'id': ['r10'], 'printStatement': ['r10']}, 21: {'+': ['s19', 'r6'], '$': ['r6'], '(': ['r6'], ')': ['r6'], 'id': ['r6'], 'printStatement': ['r6']}, 22: {'$': ['r1'], 'printStatement': ['r1'], '(': ['r1'], 'id': ['r1']}}
parser = Parser("slr-fatal-err-2.yalp")
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

