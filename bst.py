# Binary Search Tree Node
class BSTNode:
	def __init__(self, val):
		self.val = val # data value of node
		self.left = None # left child
		self.right = None # right child


# Binary Search Tree Implementation
class BST:
	def __init__(self, root):
		self.root = root # BST Node

	# finds the minimum element in BST
	def findMin(self):
		if self.root is None:
			return None
		return BST.getLeftMost(self.root)

	@staticmethod
	def getLeftMost(root):
		# find leftmost child
		while root.left is not None:
			root = root.left

		return root

	# finds the maximum element in BST
	def findMax(self):
		if self.root is None:
			return None
		return BST.getRightMost(self.root)

	@staticmethod
	def getRightMost(root):
		# find rightmost child
		while root.right is not None:
			root = root.right

		return root

	# searches for val in the tree
	def search(self, val):
		current = self.root

		while current is not None:
			# val larger than current? traverse through right subtree
			if val > current.val:
				current = current.right

			# val smaller than current? traverse through left subtree
			elif val < current.val:
				current = current.left

			# value found
			else:
				return current

		return None

	# finds the appropriate location of the value to be inserted in the tree and inserts once found
	def insert(self, val):
		n = BSTNode(val)

		if self.root is None:
			self.root = n
			return

		current = self.root
		while current is not None:
			parent = current
			if n.val > current.val:
				current = current.right
			else:
				current = current.left

		if n.val > parent.val:
			parent.right = n
		else:
			parent.left = n


	# deletes val from BST if it exists
	def delete(self, val):
		self.root = BST.deleteNode(self.root, val)


	@staticmethod
	def deleteNode(root, val):
		if root is None:
			return None

		# node to delete in right subtree
		if val > root.val:
			root.right = BST.deleteNode(root.right, val)
		# node to delete in left subtree
		elif val < root.val:
			root.left = BST.deleteNode(root.left, val)
		# node to delete is found
		else:
			# case #1: node to delete has one or no children
			if root.left is None:
				tmp = root.right
				return tmp
			elif root.right is None:
				tmp = root.left
				return tmp
			# case #2: node to delete has two children
			else:
				# get min el in right subtree
				minEl = BST.getLeftMost(root.right)
				root.val = minEl.val
				root.right = BST.deleteNode(root.right, minEl.val)
		return root
