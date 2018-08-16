'''
Linked list data structure. File is used as part of testing csv plugin
Author: Peter
'''
class Node:

	def __init__(self, data, node):
		self.data = data
		self.nextNode = node

	def __str__(self):
		return self.data


class LinkedList:
	def __init__(self):
		self.headNode = None

	def add(self, data):
		if self.headNode is None:
			self.headNode = Node(data, None)
		else:
			newNode = Node(data, self.headNode)
			self.headNode = newNode

	def add_in_order(self, data):
		#print('Inserting {}'.format(data))
		if self.headNode is None:
			self.headNode = Node(data, None)
		else:
			#print("Success... {}".format(self.insert(data)))
			currentNode = self.headNode
			previousNode = None
			while currentNode is not None:
				if data < currentNode.data:
					if previousNode is None:
						newNode = Node(data, currentNode)
						self.headNode = newNode
						return True
					else:	
						newNode = Node(data, currentNode)
						previousNode.nextNode = newNode
						return True
				else:
					if currentNode.nextNode is None:
						#if data >= currentNode.data:
						newNode = Node(data, None)
						currentNode.nextNode = newNode
						return True
				previousNode = currentNode	
				currentNode = currentNode.nextNode
			return False				

	def printList(self):
		currentNode = self.headNode
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.nextNode


def main():
	newList = LinkedList()
	arr = [7, 3, 8, 4, 9, 6, 2, 6, 9, 12, 23, 42, 3, 2, 45, 26, 14, 35, 34, 21, 56, 24, 31, 19]
	arr = [3,2,1]
	for num in arr:
		newList.add_in_order(num)
	newList.printList()

if __name__ == '__main__':	main()
