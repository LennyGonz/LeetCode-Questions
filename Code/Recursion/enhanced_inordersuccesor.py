def inorderSuccessor(root, p):
  successor = None
  while root:
    if p.val >= root.val:
      root = root.right
    
    else:
      successor = root
      root = root.left
