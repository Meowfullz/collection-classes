from queues.queue import  *
from node.node import *
from stack.stack import *
from queues.palindrome import *
from loops import *
from recursion import *
def main():
	santaClaus()
	# getPalindromes()
	loopsrecursive()



def santaClaus():
	#Q1
	s = node('A', None)
	s.addNodeAfter('T')
	s.addNodeAfter('N')
	s.addNodeAfter('A')
	s.addNodeAfter('S')

	#Q2
	c = node('S', None)
	c.addNodeAfter('U')
	c.addNodeAfter('A')
	c.addNodeAfter('L')
	c.addNodeAfter('C')

	#Q3
	selection = s

	#Q4
	selection = selection.getLink()
	selection = selection.getLink()
	selection = selection.getLink()
	selection = selection.getLink()

	#Q5 
	selection.setLink(c)


def loopsrecursive():
	print('LOOP')
	print(evens(-10,10))

	print('RECURSION')
	print(evensrecursion(-10,10))


def getPalindromes():
	words = list(map(str, input("Enter ten words separated by a space: ").split()))

	while True:
		for x in words:

			if (palindrome.isPalindrome(x)):
				print(x, ' Is a Palindrome')
		else: 
			print(x, 'Not a Palindrome')
		if not x:
			break


if __name__ == "__main__":
	main()