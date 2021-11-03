def traverse(root, hd_table, distance=0, level=0):
  if not root:
    return []

  if distance not in hd_table or hd_table[distance][1] <= level:
    hd_table[distance] = (root.val, level)

  traverse(root.left, hd_table, distance - 1, level + 1)
  traverse(root.right, hd_table, distance + 1, level + 1)

  return hd_table

def get_bottom_view(root):
  hd_table = traverse(root, {})

  min_hd, max_hd = min(hd_table), max(hd_table)
  return [hd_table[k][0] for k in range(min_hd, max_hd + 1)]
