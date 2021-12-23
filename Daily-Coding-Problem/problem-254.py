class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def convert(root):
  if not root:
    return None

  root.left = convert(root.left)
  root.right = convert(root.right)

  if not root.left and not root.right:
    return root

  if root.left and root.right:
    return root

  if not root.left:
    root = root.right
  else:
    root = root.left

'''
Since we visit each node once, this will take O(N) time. The space complexity will be how far down we recur, which is equal to the height of the tree.
'''
