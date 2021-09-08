def min_sum_path(node):
  return list(reversed(_min_sum_path(node)))

def _min_sum_path(node):
  if node:
    left_list = _min_sum_path(node.left)
    right_list = _min_sum_path(node.right)

    min_list = min(left_list, right_list, key=lambda lst: sum(node.val for node in lst))
    min_list.append(node)

    return min_list

  return []
