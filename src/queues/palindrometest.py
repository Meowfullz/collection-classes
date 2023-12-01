from queues.queue import  *
from stack.stack import *

class palindrome:
	@staticmethod
	def isPalindrome(expression: str):
		q = queue()  #Queue to read the expression forward
		s = stack() #Stack to read the expression backward
		m = queue()


		mismatches = 0 # used to keep track of the differences in the queue and stack

		# convert expression to upper-case
		expression = expression.upper()

		# loop through the expression a character at a time
		for e in expression:
			# if the current character is an alphabetic character
			if e.isalpha():
				# push it onto the stack and add it to the queue
				s.push(e)
				q.enqueue(e)
				m.enqueue (e)
				
		# while queue isn't empty
		while (not q.isEmpty()):
			if (q.dequeue() != s.pop()):
				# increment mismatches
				mismatches += 1
				m.dequeue()
				print('Mistmatch detected at', m.getData())
				break

	

		


			
		
		# return True if mismatches is equal to 0, else return False
		return (mismatches == 0)
		
