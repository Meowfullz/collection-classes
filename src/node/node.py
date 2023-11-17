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

	def addNodeAfter(self, element):
		"""Adds a new node containing a specified element value at a
		selected position in the calling node.

		Args:
			element (_type_): specified element value
		"""		
		self.__link = node(element, self.__link)

	def removeNodeAfter(self):
		"""Removes a node from a slected position in the calling node.
		"""		
		self.__link = self.__link.__link
	
	@staticmethod
	def listlength(head):
		"""Computes and returns the number of nodes in a specified node

		Args:
			head (node): specified Node

		Returns:
			int: number of nodes
		"""
		cursor = head # cursor used to step through the specified node
		length = 0 # used to count the nodes

		# step through the nodes in the specified node as long as the
		# cursor isnt null
		while (cursor != None):
			#increment length
			length += 1

			# move cursor to next node
			cursor = cursor.getLink()

		# return length
		return length

	@staticmethod
	def listSearch(head, target):
		"""Searches for a specified target in a specified node

		Args:
			head (node): specified node
			target: specified target

		Returns:
		node: reference to node that contains specified target value
		if specified target value is found, else None
		"""	

		cursor = head # cursor used to step through the specified node

		# step through the nodes in the specified node as long as the
		# cursor isn't None
		while (cursor != None):
			# check if thee data value in the node cursor reveres to is equal
			# to the target
			if (cursor.getData()== target):
				# return cursor 
				return cursor
			# move cursor to next node
			cursor = cursor.getLink()

		# return None
		return None
	
	@staticmethod
	def listpostion(head, position: int):
		"""Searches for a node in a specified node based on a specified position

		Args:
			head (node): specified node
			position (int): specified position

		Raises:
			ValueError: indicates position is less than  one

		Returns:
		node: reference to node at specified position if specified position
		is found, else None
		"""		
		cursor = head # used to step through the specified node
		i = 1 # used to count the nodes
		
		try:
			# if a position is less than 1 raise error
			if (position < 1):
				raise ValueError("Position may not be less than 1.")
		except ValueError as e:
			# display error and exit
			exit(e)
		else: 
			#move cursor forward the correct number of nodes
			# as long as i is less than position and cursor isnt 
			# equal to None
			#if cursor becomes None that means the spcified position
			# was greater than the number of nodes in the spcified node
			while ((i < position) and (cursor != None)):
				#move the cursor to the next node
				cursor = cursor.getLink()
				# increment counter variable
				i+= 1
			# return cursor
			return cursor 
	
	@staticmethod
	def listCopy(source):
		"""Make a copy of a specified node.
		
		Args:
			source (node): specified node
			
		Returns:
			node: references to the head node in the copy
		"""

		# if specified node is None, return None
		if (source is None):
			return None
		
		# make copy head refer to a node that ontains the same
		# data value in the spcified source node to be copied
		copyHead = node(source.getData(), None)
		# make copy tail refer to the same node as copy head
		copyTail = copyHead

		# keep looping through the specified source node to be copied
		# until we reach the node that has a link of None
		while (source.getLink() != None):
			# advance to the next node in the specified source node to be copied
			source = source.getLink()
			# get the data value in the specified osurce node and add it to the 
			# end of copy tail
			copyTail.addNodeAfter(source.getData())
			# advance copy tail to the next node
			copyTail = copyTail.getLink()
		# return copy head
		return copyHead
	
	@staticmethod
	def listCopyWithTail(source):
		"""Makes a copy of a specified node
		
		Args:
			source (node): specified node to be copied
			
		Returns:
			[node]: references to head and tail of the copy"""
		# if specified node is None, return None
		if (source is None):
			return None
		
		# make copy head refer to a node that ontains the same
		# data value in the spcified source node to be copied
		copyHead = node(source.getData(), None)
		# make copy tail refer to the same node as copy head
		copyTail = copyHead

		# keep looping through the specified source node to be copied
		# until we reach the node that has a link of None
		while (source.getLink() != None):
			# advance to the next node in the specified source node to be copied
			source = source.getLink()
			# get the data value in the specified osurce node and add it to the 
			# end of copy tail
			copyTail.addNodeAfter(source.getData())
			# advance copy tail to the next node
			copyTail = copyTail.getLink()

		# return copy head and copy tail
		return [copyHead, copyTail]
	
	def setDataAtPosition(self, position: int, data):
		"""Sets the data value stored in the calling node at the specified position 
		to the specified data value.

		Args:
			position (int): specified posotion
			data: specified data value

		Raises:
			ValueError: indicates position is less than one
		"""        
		cursor = self   # used to step through calling node
		i = 1           # used to count nodes

		try:       
			# if position is less than one, raise error   
			if (position < 1):
				raise ValueError("Position may not be less than 1.")
		except ValueError as e:
			# display error and exit
			exit(e)
		else:
			# move cursor forward the correct number nodes
			# keep looping as long as i is less than specified position 
			# and cursor isn't equal to None
			# if cursor becomes None that means specified position was greater than
			# number of nodes in specified node
			while ((i < position) and (cursor != None)):
				# move cursor to next node
				cursor = cursor.getLink()
				# increment counter
				i = i + 1

			# set data value in node cursor refers to
			cursor.setData(data)

