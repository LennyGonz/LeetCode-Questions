def invert(node):
  if not node:
    return node

  left = invert(node.left)
  right = invert(node.right)

  node.left, node.right = right, left
  return node
