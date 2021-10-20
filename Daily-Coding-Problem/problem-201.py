def max_path_weight(arrays):
  for level in range(len(arrays) - 2, -1, -1):
    for index in range(level + 1):
      arrays[level][index] += max(arrays[level + 1][index], arrays[level + 1][index + 1])

  return arrays[0][0]
