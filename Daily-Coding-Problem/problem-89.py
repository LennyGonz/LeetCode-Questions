import math

def isValid(root):
  def validate(root, low, high):
    if not root:
      return True
    
    if root.val <= low or root.val >= high:
      return False
    
    return validate(root.left, low, root.val) and validate(root.right, root.val, high)
  
  validate(root, -math.inf, math.inf)

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  def is_bst_helper(root, min_key, max_key):
    if root is None:
      return True
    if root.key <= min_key or root.key >= max_key:
      return False
    return is_bst_helper(root.left, min_key, root.key) and is_bst_helper(root.right, root.key, max_key)

  return is_bst_helper(root, float('-inf'), float('inf'))
