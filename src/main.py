from node.node import *

def main():
	# testinit()
	# testGettersAndSetters()
	testAddNodeAfter()

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