def inorderTraversal(root):
  res = []
  helper(root, res)
  return res

def helper(root, res):
  if root:
    helper(root.left, res)
    res.append(root.val)
    helper(root.right, res)
