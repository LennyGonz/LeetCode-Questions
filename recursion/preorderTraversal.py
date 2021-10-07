def preorderTraversal(root):
  res = []
  helper(root, res)
  return res

def helper(root, res):
  if root:
    res.append(root.val)
    helper(root.left, res)
    helper(root.right, res)
