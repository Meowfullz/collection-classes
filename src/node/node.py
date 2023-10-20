class node:
	"""The node class holds a collection of values using nodes. It is going to include methods that allow the node to 
	be manipulated and modified
	"""

	def __init__(self, data, link):
		"""Constructs a node using the specified data values and link

		:ivar __data: data values of node
		:ivar __link: link portion of the node

		Args:
			data: specified data value
			link: specified link 
		"""		
		self.__data = data
		self.__link = link

	def getData(self):
		"""returns the data value stored in the calling node to the specified data

		Returns:
			_type_: data value stored in the calling node
		"""		
		return self.__data
	
	def setData(self, data):
		"""sets the data value stored in the calling node to the specified
		data value

		Args:
			data (_type_): specified data value
		"""		
		self.__data = data

	def getLink(self):
		"""Returns the link stored in the calling node

		Returns:
			node: link stored in the calling node
		"""		
		return self.__link
	
	def setLink(self, link):
		"""Sets the data value stored in the calling node to the specified data value

		Args:
			link (_type_): specified data value
		"""		
		self.__link = link
