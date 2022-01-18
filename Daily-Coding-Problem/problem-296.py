class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def make_bst(array):
  if not array:
    return None

  mid = len(array) // 2

  root = Node(array[mid])
  root.left = make_bst(array[:mid])
  root.right = make_bst(array[mid + 1:])

  return root

'''
This algorithm will take O(N) time and space, since for each element of the list, we must construct a node and add it as a child to the tree, each of which can be considered O(1) operations.
'''
