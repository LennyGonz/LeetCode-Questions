def infer_area(cache):
  max_area = 0
  for i in range(len(cache)):
    for j in range(i + 1, len(cache) + 1):
      current_rectangle = min(cache[i:j]) * (j - i)
      max_area = max(max_area, current_rectangle)
  return max_area


def largest_rectangle(matrix):
  n, m = len(matrix), len(matrix[0])
  max_so_far = 0

  cache = [0 for _ in range(m)]
  for row in matrix:
    for i, val in enumerate(row):
      if val == 0:
        cache[i] = 0
      elif val == 1:
        cache[i] += 1
    max_so_far = max(max_so_far, infer_area(cache))

  return max_so_far
