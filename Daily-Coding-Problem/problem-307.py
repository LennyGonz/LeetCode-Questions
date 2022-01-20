class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def get_bounds(root, x, floor=None, ceil=None):
  if not root:
    return floor, ceil

  if x == root.data:
    return x, x

  elif x < root.data:
    floor, ceil = get_bounds(root.left, x, floor, root.data)

  elif x > root.data:
    floor, ceil = get_bounds(root.right, x, root.data, ceil)

  return floor, ceil

'''
This algorithm requires a single traversal from the top to the bottom of the tree. 
Therefore, the time complexity will be O(h), where h is the height of the tree.
If the tree is balanced, this is equal to O(log N).

Similarly, the space complexity will be O(h), since we will need to make space on the stack for each recursive call.
'''
