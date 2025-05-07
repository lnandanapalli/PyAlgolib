class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"Key: {self.key}"


class BinarySearchTree:
    def __init__(self):
        self.root = None
        return self.root

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def search(self, node, key):
        if node is None:
            return node
        if key == node.key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def minimum(self, node):
        if node is None:
            return None
        if node.left is None:
            return node
        else:
            return self.minimum(node.left)

    def maximum(self, node):
        if node is None:
            return None
        if node.right is None:
            return node
        else:
            return self.maximum(node.right)


# Manually creating dummy nodes for testing
bst = BinarySearchTree()

# Creating a sample tree:
#         10
#        /  \
#       5    15
#      / \   / \
#     2   7 12 20

bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(2)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)
bst.root.right.right = Node(20)

print("Inorder traversal of the BST:")
bst.inorder_traversal(bst.root)

print(bst.search(bst.root, 21))
