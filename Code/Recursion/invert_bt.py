def invert(root):
  if root is None:
    return
  
  root.left = root.right
  root.right = root.left
  
  invert(root.left)
  invert(root.right)

  return root
