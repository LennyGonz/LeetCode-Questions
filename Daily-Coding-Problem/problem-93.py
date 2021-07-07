class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def largest_bst_subtree(root):
  max_size = 0
  max_root = None
  def helper(root):
    # Returns a tuple of (size, min_key, max_key) of the subtree.
    nonlocal max_size
    nonlocal max_root
    if root is None:
      return (0, float('inf'), float('-inf'))
    left = helper(root.left)
    right = helper(root.right)
    if root.key > left[2] and root.key < right[1]:
      size = left[0] + right[0] + 1
      if size > max_size:
        max_size = size
        max_root = root
      return (size, min(root.key, left[1]), max(root.key, right[2]))
    else:
      return (0, float('-inf'), float('inf'))

  helper(root)
  return max_root
