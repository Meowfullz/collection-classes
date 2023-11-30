from queues.queue import  *
from stack.stack import *

class palindrome:

	
	@staticmethod
	def isPalindrome(expression: str):


		q = queue()  #Queue to read the expression forward
		q2 = queue() #Stack to read the expression backward
		mismatches = 0

		expressionreversed = expression[::-1]
		for e in expressionreversed:
			q2.enqueue(e)

		for x in expression:
			q.enqueue(x)
		
		while (not q.isEmpty() and q2.isEmpty()):
			
			if (q.dequeue() != q2.dequeue()):
				# increment mismatches
				mismatches += 1
		return (mismatches == 0)



	


