def find_depth(tree):
  max_depth = depth = 0

  for char in tree:
    if char == '(':
      depth += 1
    elif char == ')':
      depth -= 1
    max_depth = max(max_depth, depth)

  return max_depth
