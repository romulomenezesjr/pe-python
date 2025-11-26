class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(4)
    bt.root.left = Node(3)
    bt.root.right = Node(8)
    
    bt.root.left.left = Node(2)
    bt.root.left.right = None
    bt.root.right.left = Node(7)
    bt.root.right.right = Node(9)


    bt.preorder_traversal(bt.root) 