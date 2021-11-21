class Node:
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children

def is_symmetric(left, right):
  if left.val != right.val:
    return False

  if not left.children and not right.children:
    return True

  if len(left.children) != len(right.children):
    return False

  k = len(left.children)
  for i in range(k):
    if not is_symmetric(left.children[i], right.children[k - 1 - i]):
      return False

  return True

assert is_symmetric(root, root)
