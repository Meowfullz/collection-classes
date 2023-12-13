@staticmethod
def evensrecursion (start: int, end: int):
	"""Finds and displays the even numbers between a specified
	starting and ending value.
	Args:
	start (int): specified starting value
	end (int): specified ending value
	"""
	i = start
	if start > end:
		return
	if start % 2 == 0:
		print(start, end=" ")
	evensrecursion(start + 1, end)