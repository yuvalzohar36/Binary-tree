#Binary Tree Project 
#Currently Without Viusalize
import random

class Tree():
		def __init__ (self):
				self.root = None

		def add_value(self, val):
				n = Node(val)
				if (self.root == None):
                                  self.root = n
				else:
				  self.root.addNode(n)

		def traverse(self):
			self.root.visit()

		def search_tree(self,val):
			found = self.root.search(val)
			return found


class Node():
		def __init__ (self, val):
				self.value = val
				self.left = None
				self.right = None

		def visit(self):
				if (self.left != None):
						self.left.visit()
				print(self.value)
				if (self.right != None):
						self.right.visit()

		def addNode(self, n):
				if (n.value < self.value):
						if (self.left == None):
								self.left =n
						else:
								self.left.addNode(n)
				elif (n.value > self.value):
						if (self.right == None):
								self.right =n
						else:
								self.right.addNode(n)

		def search(self, val):
			if (self.value == val):
				print("Value found : " + str(val))
				return self

			elif (val<self.value and self.left != None):
				return self.left.search(val)
			elif (val > self.value and self.right != None):
				return self.right.search(val)
			return None


if __name__ == '__main__':
		tree = Tree()
		for i in range(5):
				value = random.randint(0,10)
				tree.add_value(value)
				
		tree.traverse()
		tree.search_tree(5)

