def two_sum(root, K):
  for node_one in iter_tree(root):
    node_two = search(root, K - node_one.val)

    if node_two:
      return (node_one, node_two)

  return None


def search(node, val):
  if not node:
    return None

  if node.val == val:
    return node
  elif node.val < val:
    return search(node.right, val)
  else:
    return search(node.left, val)
