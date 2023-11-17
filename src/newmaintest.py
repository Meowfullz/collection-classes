from node.node import *
from stack.stack import *
from stack.balanceparems import *
from stack.calculator import *
from stack.serialsearch import *
from stack.selectionsort import *

def main():
	testSelectionSort()



def testSelectionSort():
	# create an empty stack
	s = stack()
	# initialize first
	first = 1
	# push -7 onto the top of the stack
	s.push(-7)
	# push 42 onto the top of the stack
	s.push(42)
	# push 70 onto the top of the stack
	s.push(70)
	# push 39 onto the top of the stack
	s.push(39)
	# push 3 onto the top of the stack
	s.push(3)
	# push 63 onto the top of the stack
	s.push(63)
	# push 8 onto the top of the stack
	s.push(8)
	# print unsorted stack
	print('Stacks:', s)
	# call selection sort methods
	selectionsort(s, first)

	# create an empty stack
	s = stack()
	# initialize first
	first = 4
	# push -7 onto the top of the stack
	s.push(-7)
	# push 42 onto the top of the stack
	s.push(42)
	# push 70 onto the top of the stack
	s.push(70)
	# push 39 onto the top of the stack
	s.push(39)
	# push 3 onto the top of the stack
	s.push(3)
	# push 63 onto the top of the stack
	s.push(63)
	# push 8 onto the top of the stack
	s.push(8)
	# print unsorted stack
	print('Stacks:', s)
	# call selection sort methods
	selectionsort(s, first)

	# create an empty stack
	s = stack()
	# initialize first
	first = 6
	# push -7 onto the top of the stack
	s.push(-7)
	# push 42 onto the top of the stack
	s.push(42)
	# push 70 onto the top of the stack
	s.push(70)
	# push 39 onto the top of the stack
	s.push(39)
	# push 3 onto the top of the stack
	s.push(3)
	# push 63 onto the top of the stack
	s.push(63)
	# push 8 onto the top of the stack
	s.push(8)
	# print unsorted stack
	print('Stacks:', s)
	# call selection sort methods
	selectionsort(s, first)



	# print sorted stack

if __name__ == "__main__":
	main()