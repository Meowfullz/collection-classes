from node.node import *
from stack.stack import *
from stack.balanceparems import *

def main():
	#testPush()
	#testPop()
	#testIsEmpty()
	#testPeek()
	print('Parenthesis are balanced?', balancedparens.isBalanced('{X+Y')) #False
	print('Parenthesis are balanced?', balancedparens.isBalanced('{X+Y)')) #False
	print('Parenthesis are balanced?', balancedparens.isBalanced('{X+Y}*Z')) #True
	print('Parenthesis are balanced?', balancedparens.isBalanced('[A+B]*({X+Y}*Z)'))


def testPeek():
	print('Testing peek method in stack class')
 
	s=stack()
	print('Stack size is', s.size())
	print('Stack contains:', s)

	s.push('S')
	print('Stack size is', s.size()) #1
	print('Stack contains:', s) #[S]
	print('Top element in stack is:', s.peek()) # S

	s.push('B')
	print('Stack size is', s.size()) #2
	print('Stack contains:', s)  #[B S]
	print('Top element in stack is:', s.peek())  # BS

	s.push('O')
	print('Stack size is', s.size()) #3
	print('Stack contains:', s) #[OBS]
	print('Top element in stack is:', s.peek()) # OBS

	s.push('J')
	print('Stack size is', s.size()) #4
	print('Stack contains:', s) #[J O B S]
	print('Top element in stack is:', s.peek()) # JOBS

	


def testIsEmpty():
	print('Testing Is Empty in Stack Class')
	s = stack()
	s.push('S')
	s.push('B')
	s.push('O')
	s.push('J')

	print('Stack size is', s.size()) #4
	print('Stack contains:', s) #[J O B S]

	while(not s.isEmpty()):
		print('Just popped:', s.pop())

	print('Stack size is: ', s.size()) #0
	print('Stack Contains: ', s) #[]

def testPop():
	print('Testing Pop Method in Stack class')
	s = stack()
	s.push('S')
	s.push('B')
	s.push('O')
	s.push('J')

	print('Stack size is', s.size()) #4
	print('Stack contains:', s) #[J O B S]
	print('Just popped', s.pop()) #J

	print('Stack size is', s.size()) #3
	print('Stack contains:', s) #[O B S]
	print('Just popped', s.pop()) #O

	print('Stack size is', s.size()) #2
	print('Stack contains:', s) #[B S]
	print('Just popped', s.pop()) #B

	print('Stack size is', s.size()) #1
	print('Stack contains:', s) #[S]
	print('Just popped', s.pop()) #S

	print('Just popped', s.pop()) 

def testPush():
	print("Testing Push Method in Stack Class")

	s = stack()
	print("Stack size is", s.size()) #0
	print("Stack contains:", s)  #[]

	s.push('S')
	
	print("Stack size is", s.size()) #1
	print("stack contains:", s)      #[S]

	#s.push('B')
	s.push(1)
	print("Stack size is", s.size()) #2
	print("stack contains:", s)      #[B, S]

	#s.push('O')
	s.push((1,2))
	print("Stack size is", s.size()) #3
	print("stack contains:", s)      #[O, B, S]

	#s.push('J')
	s.push([1,2,3])
	print("Stack size is", s.size()) #4
	print("stack contains:", s)      #[J, O, B, S]




def assignment():
	#Question 1
	head = node(2, None)
	head = node("=", head)
	head = node(1, head)
	head= node("+", head)
	head= node(1, head)

	#Question 2
	operator = head

	#Question 3
	operator = operator.getLink()

	#Question 4
	result=head

	#Question 5
	result = result.getLink()
	result = result.getLink()
	result = result.getLink()
	result = result.getLink()

	#QUestion 6
	operator.setData('-')
	result.setData(0)

	#Question 7
	operator.setData('*')
	result.setData(1)

	# QUestion 8
	operator.setData('/')
	result.setData(1)

	#Question 9
	head.setData(7)
	result.setData(7)

	#Question 10
	operator = operator.getLink()

	#Question 11
	operator.removeNodeAfter()
	head.removeNodeAfter()

	#question 12
	print('Head contains', node.listlength(head), 'Nodes')
	print('Operator contains', node.listlength(operator), 'Nodes')
	print('Result contains', node.listlength(result), 'Nodes')

	#Question 13
	print("Head Contains Character", node.listSearch(head, 1).getData())
	print("Operator Contains Character", node.listSearch(operator, 1).getData())
	if (node.listSearch(result, 1) != None):
		print("Result Contains", node.listSearch(result, 1).getData())
	else:
		print("Result doesn't contain 1.")

	#Question 14
	copy0=head.listCopy
	copy1=result.listCopy

	#Question 15
	print('Copy0 contains', node.listlength(head), 'Nodes')
	print('Copy1 contains', node.listlength(result), 'Nodes')
	

	
def testListCopyWithTail():
	print('Testing List Copy')
	#construct a node with data equal to S and link equal to None
	# and assign its reference to head
	source = node('S', None)

	# construct a node with data equal to B and link equal to head
	# and assign its reference to head
	source = node("B", source)

	# construct a node with data equal to O and link equal to head
	# and assign its reference to head
	source = node('O', source)

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	source = node('J', source)

	copy = node.listCopyWithTail(source)
	print("Source contains", node.listpostion(source, 1).getData(),
		node.listpostion(source, 2).getData(),
		node.listpostion(source, 3).getData(),
		node.listpostion(source, 4).getData())
	
	print("Copy head contains", node.listpostion(copy[0], 1).getData(),
		node.listpostion(copy[0], 2).getData(),
		node.listpostion(copy[0], 3).getData(),
		node.listpostion(copy[0], 4).getData())

	print("Copy tail contains", node.listpostion(copy[1], 1).getData())

def testListCopy():
	print('Testing List Copy')
	#construct a node with data equal to S and link equal to None
	# and assign its reference to head
	source = node('S', None)

	# construct a node with data equal to B and link equal to head
	# and assign its reference to head
	source = node("B", source)

	# construct a node with data equal to O and link equal to head
	# and assign its reference to head
	source = node('O', source)

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	source = node('J', source)

	copy = node.listCopy(source)
	print("Source contains", node.listpostion(source, 1).getData(),
		node.listpostion(source, 2).getData(),
		node.listpostion(source, 3).getData(),
		node.listpostion(source, 4).getData())
	
	print("Copy contains", node.listpostion(copy, 1).getData(),
		node.listpostion(copy, 2).getData(),
		node.listpostion(copy, 3).getData(),
		node.listpostion(copy, 4).getData())


def testListPosition():
	print('Testing List Position')
	#construct a node with data equal to S and link equal to None
	# and assign its reference to head
	head = node('S', None)

	# construct a node with data equal to B and link equal to head
	# and assign its reference to head
	head = node("B", head)

	# construct a node with data equal to O and link equal to head
	# and assign its reference to head
	head = node('O', head)

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	head = node('J', head)
	print(' First node contains data:', node.listpostion(head, 1).getData())
	print(' Second node contains data:', node.listpostion(head, 2).getData())
	print(' Third node contains data:', node.listpostion(head, 3).getData())
	print(' Fourth node contains data:', node.listpostion(head, 4).getData())
	if (node.listpostion(head,5) != None):
		print ('Fourth node contains data:', node.listpostion(head, 5).getData())
	else: 
		print("There is no fifth node.")

def testlistSearch():
	print('Testing List Search')
	#construct a node with data equal to S and link equal to None
	# and assign its reference to head
	head = node('S', None)

	# construct a node with data equal to B and link equal to head
	# and assign its reference to head
	head = node("B", head)

	# construct a node with data equal to O and link equal to head
	# and assign its reference to head
	head = node('O', head)

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	head = node('J', head)

	print("Head Contains", node.listSearch(head, 'J').getData())
	print("Head Contains", node.listSearch(head, 'O').getData())
	print("Head Contains", node.listSearch(head, 'B').getData())
	print("Head Contains", node.listSearch(head, 'S').getData())

	if (node.listSearch(head, 'Z') != None):
		print("Head Contains", node.listSearch(head, 'Z').getData())
	else:
		print("Head doesn't contain Z.")

def testListLength():
	print('Testing List Length')

	#construct a node with data equal to S and link equal to None
	# and assign its reference to head
	head = node('S', None)

	# construct a node with data equal to B and link equal to head
	# and assign its reference to head
	head = node("B", head)

	# construct a node with data equal to O and link equal to head
	# and assign its reference to head
	head = node('O', head)

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	head = node('J', head)

	print("Length of head is:", node.listlength(head))

	# construct 
def review():
	print('Review')

	#Q1 
	head = node('X', None)
	head = node('X', head)
	head = node('X', head)
	head = node('X', head)

	#Q2 
	selection1 = head

	#Q3
	selection1.addNodeAfter('O')

	# Q4 
	selection1 = selection1.getLink()
	selection1 = selection1.getLink()

	# Q5
	selection1.addNodeAfter('O')

	#Q6 
	selection1 = selection1.getLink()
	selection1 = selection1.getLink()

	#Q7
	selection1.addNodeAfter('O')

	#Q8 
	tail = head

	#Q9
	tail = tail.getLink()
	tail = tail.getLink()
	tail = tail.getLink()
	tail = tail.getLink()
	tail = tail.getLink()
	tail = tail.getLink()

	#Q10 
	selection2 = head

	#Q11 
	selection2 = selection2.getLink()
	selection2 = selection2.getLink()

	#Q12  
	head.setData('A')
	selection2.setData('A')
	selection1.setData('A')
	tail.setData('A')

	# Q13
	head.removeNodeAfter()
	selection1.removeNodeAfter()

def testRemoveNodeAfter():
	print ("Testing Remove Node After")

	# construct a node with data equal to S and link equal to none
	# and assign its reference to head
	head = node('S', None) #S

	# Construct a node with data equal to B and link equal to head
	# and assign its reference to head 
	head = node('B', head) # B -> S

	# construct a node with data equal to O and link equal to head 
	# and assign its reference to head
	head = node ('O', head) # o -> B - > S

	# construct a node with data equal to J and link equal to head
	# and assign its reference to head
	head = node('J', head) # j > o > B > S

	print('The head node contains data:', head.getData())

	# remove the node after the node head refers to (node that has data equal to O)
	head.removeNodeAfter() # J > B > S

	head = head.getLink() # B > S

	print("THe head node contains data:", head.getData())

	# remove the node after the node head refers to (node that has data equal to O)
	head.removeNodeAfter() 
	print('the head node contains data:', head.getData()) 

	""" # remove the node after the node head refers to (node tahat has data equal to S)
	head.removeNodeAfter() this line of code will generate an Attribute Error """
	



def testAddNodeAfter():
	print("Testing add node after")
	# constructs a node with data equal to J and link equal to none
	# and assign its reference to head
	head = node ("J", None) # J

	print("The head node contains data:", head.getData())

	# declare a new node named selection and make it refer
	# to the same node as head
	selection = head
	
	print("The head node contains data:", head.getData())
	print("The selection node contains data:", selection.getData())

	# add a node with data equal to 0 after the node selection
	# refers to
	selection.addNodeAfter('O') # J -> O

	# get selections link and assign its reference back to selection
	selection = selection.getLink() # O

	print("The head node contains data:", head.getData())
	print("The selection node contains data:", selection.getData())

	# add a node with data equal to B after the node selection
	# refers to
	selection.addNodeAfter('B') # O -> B

	# get selections link and assign its reference back to selection
	selection = selection.getLink() # B

	print("The head node contains data:", head.getData())
	print("The selection node contains data:", selection.getData())

	# add a node with data equal to S after the node selection
	# refers to
	selection.addNodeAfter('S') # B -> S

	# get selections link and assign its reference back to selection
	selection = selection.getLink() # S

	print("The head node contains data:", head.getData())
	print("The selection node contains data:", selection.getData())

	# Declare a new node named Tail and make it refer to the same node as head
	tail = head

	# get tails link and assign its reference to tail
	tail = tail.getLink()
	tail = tail.getLink()
	tail = tail.getLink()

	# add a new node with data equal to Z after the node tail
	# refers to
	tail.addNodeAfter('Z')

	# get tails link and assign its reference to tail
	tail=tail.getLink()

	print("The head node contains data:", head.getData())
	print("The selection node contains data:", selection.getData())
	print("The tail node contains data:", tail.getData())

def testGettersAndSetters():
	print('Testing Getters and Setters')
	# constructs a node with data equal to R and link equal to none
	# and assign its reference to head
	head = node ("R", None) # R

	print("The head node contains data:", head.getData())

	head.setData('S')
	print("The head node contains data:", head.getData())

	head = node('B', head) # B -> S
	print("The head node contains data:", head.getData())

	head = node('O', head) # O -> B -> S
	print("The head node contains data:", head.getData())

	head = node('J', head) # J -> O -> B -> S
	print("The head node contains data:", head.getData())

	# get head's link and assign its reference back to head
	head = head.getLink() # O -> B -> S
	print("The head node contains data", head.getData())

	# get head's link and assign its reference back to head
	head = head.getLink() # B -> S
	print("The head node contains data", head.getData())

	# get head's link and assign its reference back to head
	head = head.getLink() #S
	print("The head node contains data", head.getData())

	# get head's link and assign its reference back to head
	""" head = head.getLink() #S
	print("The head node contains data", head.getData()) """
	print("The head node contains link:", head.getLink())

	#set heads link to a new node
	head.setLink(node('O', None)) # S -> O

def testinit():
	print("Testing init")

	# constructs a node with data equal to S and link equal to none
	# and assign its reference to head
	head = node ("S", None) # S

	#constructs a node with data equal to B and link equal to head
	# and assign its reference to head
	head = node('B', head) # B -> S

	#constructs a node with data equal to O and link equal to head
	# and assign its reference to head
	head = node('O', head) # O -> B -> S

	#constructs a node with data equal to S and link equal to head
	# and assign its reference to head
	head = node('J', head) # J -> O -> B -> S

	head = node(1, head) # 1 -> J -> O -> B -> S
	head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
	head = node([1,2], head) # [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
	head = node(('A', 'B')) # ('A', 'B') -> [1,2] -> 1.5 -> 1 -> J -> O -> B -> S

	print()
if __name__ == "__main__":
	main()