class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from queue import Queue

def print_level_order(root):
  queue = Queue()
  queue.put(root)

  while not queue.empty():
    node = queue.get()
    if node.left:
      queue.put(node.left)
    if node.right:
      queue.put(node.right)
    print(node.val)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
