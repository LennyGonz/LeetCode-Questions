def is_subtree(s, t):
  def preorder(root):
    traversal = []
    stack = [root]
    while stack:
      n = stack.pop()
      if n is None:
        traversal.append('.')  # null marker
        continue
      else:
        traversal.append(str(n.val))
      stack.append(n.right)
      stack.append(n.left)
    return ',' + ','.join(traversal) + ','  # Wrap result

  s_str = preorder(s)
  t_str = preorder(t)
  return t_str in s_str
