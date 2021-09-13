def prune(root):
  if root is None:
    return root

  root.left, root.right = prune(root.left), prune(root.right)

  if root.left is None and root.right is None and root.val == 0:
    return None

  return root
