from queues.queue import  *
from queues.palindrome import *
def main():
	# testEnqueue()
	# print('\n')
	# testQueueIsEmpty()
	# print('\n')
	# testingPeekQueue()
	# print('\n')
	# testDequeue()
	testPalindrome()

def testPalindrome():
	exp = input("Please enter an expression: ")

	if (palindrome.isPalindrome(exp)):
		print('Your expression is a palindrome.')
	else:
		print('Your expression is not a palindrome.')


def testEnqueue():
	print("Testing enqueue Method in queue Class")

	s = queue()
	print("Queue size is", s.size()) #0
	print("Queue contains:", s)  #[]

	s.enqueue('H')
	
	print("Queue size is", s.size()) #1
	print("Queue contains:", s)      #[H]

	s.enqueue('U')
	print("Queue size is", s.size()) #2
	print("Queue contains:", s)      #[H U]

	s.enqueue('R')
	print("Queue size is", s.size()) #3
	print("Queue contains:", s)      #[H U R]

	s.enqueue('B')
	print("Queue size is", s.size()) #4
	print("Queue contains:", s)		# H U R B

def testQueueIsEmpty():
	print('Testing Is Empty in Queue Class')
	s = queue()
	s.enqueue('H')
	s.enqueue('U')
	s.enqueue('R')
	s.enqueue('B')

	print('Queue size is', s.size()) #4
	print('Queue contains:', s) #[H U R B]

	while(not s.isEmpty()):
		print('Just dequeued:', s.dequeue())

	print('Queue size is: ', s.size()) #0
	print('Queue Contains: ', s) #[]

def testDequeue():
	print('Testing dequeue Method in queue class')
	s = queue()
	s.enqueue('B')
	s.enqueue('R')
	s.enqueue('U')
	s.enqueue('H')

	print('Queue size is', s.size()) #4
	print('Queue contains:', s) #[BRUH]
	print('Just dequeued', s.dequeue()) #B

	print('Queue size is', s.size()) #3
	print('Queue contains:', s) #[R U H]
	print('Just dequeued', s.dequeue()) #R

	print('Queue size is', s.size()) #2
	print('Queue contains:', s) #[U H]
	print('Just Dequeued', s.dequeue()) #U

	print('Queue size is', s.size()) #1
	print('Queue contains:', s) #[H]
	print('Just dequeued', s.dequeue()) #H

	print('Just dequeued', s.dequeue()) 


def testingPeekQueue():
	print('Testing peek method in queue class')
 
	s=queue()
	print('Queue size is', s.size())
	print('Queue contains:', s)

	s.enqueue('S')
	print('Queue size is', s.size()) #1
	print('Queue contains:', s) #[S]
	print('Top element in stack is:', s.peek()) # S

	s.enqueue('B')
	print('Queue size is', s.size()) #2
	print('Queue contains:', s)  #[B S]
	print('Top element in queue is:', s.peek())  # SB

	s.enqueue('O')
	print('Queue size is', s.size()) #3
	print('Queue contains:', s) #[SBO]
	print('Top element in queue is:', s.peek()) # SBO

	s.enqueue('J')
	print('queue size is', s.size()) #4
	print('queue contains:', s) #[S B O J]
	print('Top element in queue is:', s.peek()) # JOBS



if __name__ == "__main__":
	main()