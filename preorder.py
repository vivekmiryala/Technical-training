class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrder(root):
  if root is not None:
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

preOrder(root)
