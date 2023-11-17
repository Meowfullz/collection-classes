from node.node import *
from stack.stack import*

def selectionsort (data: stack, first:int):
	"""sorts a stack from smallest to largest bypassing the nodes to the 
	left of the of first

		Args:
			data (stack): stack to be sorted
			first (int): the node position at which the sort will begin
	"""



	# loop through list as many times as specified by
	# len(data) and first
	# this loop represents the blue arrow
	while (cursor > 0):
		# set big equal to first
		big = first

		# set j equal to first + 1
		j = first + 1

		# loop through list starting with element at
		# first + 1 and continue until you reach first + i
		# this loop represents the yellow arrow
		while (j <= first + cursor):
			# if the value in data[big] is less than
			# data[j]
			if (data[big] < data[j]):
				#set big equal to j
				big = j
			
			# increment j by 1
			j += 1

		# swap the data in first + i with the data in big 
		# set temp to value in data[first + i]
		temp = data[first+cursor]

		#set data[first + i] = data[big]
		data[first+cursor] = data[big]

		#set data[big] to value in temp
		data[big] = temp

		# decrement i by 1 
		cursor -= 1