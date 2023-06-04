from sara_compis1_tools.StateAFD import StateAFD
from sara_compis1_tools.lexEval import LexEval
from sara_compis1_tools.Error import Error
import sys

mega = [StateAFD(name='init',transitions={'ε': 'A'},accepting=False,start=True, value=None),StateAFD(name='A',transitions={' ': 'B', '\t': 'B', '\n': 'B'},accepting=False,start=False, value=None),StateAFD(name='B',transitions={' ': 'B', '\t': 'B', '\n': 'B'},accepting=True,start=False, value=''),StateAFD(name='init',transitions={'ε': 'C'},accepting=False,start=True, value=None),StateAFD(name='C',transitions={'a': 'D', 'b': 'D', 'c': 'D', 'd': 'D', 'e': 'D', 'f': 'D', 'g': 'D', 'h': 'D', 'i': 'D', 'j': 'D', 'k': 'D', 'l': 'D', 'm': 'D', 'n': 'D', 'o': 'D', 'p': 'D', 'q': 'D', 'r': 'D', 's': 'D', 't': 'D', 'u': 'D', 'v': 'D', 'w': 'D', 'x': 'D', 'y': 'D', 'z': 'D', 'A': 'D', 'B': 'D', 'C': 'D', 'D': 'D', 'E': 'D', 'F': 'D', 'G': 'D', 'H': 'D', 'I': 'D', 'J': 'D', 'K': 'D', 'L': 'D', 'M': 'D', 'N': 'D', 'O': 'D', 'P': 'D', 'Q': 'D', 'R': 'D', 'S': 'D', 'T': 'D', 'U': 'D', 'V': 'D', 'W': 'D', 'X': 'D', 'Y': 'D', 'Z': 'D'},accepting=False,start=False, value=None),StateAFD(name='D',transitions={'a': 'D', 'b': 'D', 'c': 'D', 'd': 'D', 'e': 'D', 'f': 'D', 'g': 'D', 'h': 'D', 'i': 'D', 'j': 'D', 'k': 'D', 'l': 'D', 'm': 'D', 'n': 'D', 'o': 'D', 'p': 'D', 'q': 'D', 'r': 'D', 's': 'D', 't': 'D', 'u': 'D', 'v': 'D', 'w': 'D', 'x': 'D', 'y': 'D', 'z': 'D', 'A': 'D', 'B': 'D', 'C': 'D', 'D': 'D', 'E': 'D', 'F': 'D', 'G': 'D', 'H': 'D', 'I': 'D', 'J': 'D', 'K': 'D', 'L': 'D', 'M': 'D', 'N': 'D', 'O': 'D', 'P': 'D', 'Q': 'D', 'R': 'D', 'S': 'D', 'T': 'D', 'U': 'D', 'V': 'D', 'W': 'D', 'X': 'D', 'Y': 'D', 'Z': 'D', '0': 'D', '1': 'D', '2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D'},accepting=True,start=False, value='id'),StateAFD(name='init',transitions={'ε': 'E'},accepting=False,start=True, value=None),StateAFD(name='E',transitions={'+': 'F'},accepting=False,start=False, value=None),StateAFD(name='F',transitions={},accepting=True,start=False, value='+'),StateAFD(name='init',transitions={'ε': 'G'},accepting=False,start=True, value=None),StateAFD(name='G',transitions={'(': 'H'},accepting=False,start=False, value=None),StateAFD(name='H',transitions={},accepting=True,start=False, value='('),StateAFD(name='init',transitions={'ε': 'I'},accepting=False,start=True, value=None),StateAFD(name='I',transitions={')': 'J'},accepting=False,start=False, value=None),StateAFD(name='J',transitions={},accepting=True,start=False, value=')'),StateAFD(name='init',transitions={'ε': 'K'},accepting=False,start=True, value=None),StateAFD(name='K',transitions={'*': 'L'},accepting=False,start=False, value=None),StateAFD(name='L',transitions={},accepting=True,start=False, value='*')]
errors = set()

class Generated:
	def return_tokens(self):
		return ['espacioEnBlanco','id','+','(',')','*']

	def parse(self, test_file):
		lex = LexEval(test_file)
		return lex.evaluate(mega, errors)
