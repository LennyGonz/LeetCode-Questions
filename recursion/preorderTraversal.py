def preorderTraversal(root):
  res = []
  helper(root, res)
  return res

def helper(root, res):
  if root:
    helper(root.left, res)
    helper(root.right, res)
    res.append(root.val)
