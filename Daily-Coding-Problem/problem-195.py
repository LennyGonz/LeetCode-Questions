def matrix_count_edge(matrix, i1, j1, i2, j2):
  m, n = len(matrix), len(matrix[0])

  count = 0

  # Count numbers smaller than m[i1][j1]
  a = matrix[i1][j1]
  i, j = 0, m - 1
  for j in reversed(range(n)):
    while i < m and matrix[i][j] < a:
      i += 1
    count += i

  # Count numbers greater than m[i2][j2]
  b = matrix[i2][j2]
  i, j = 0, m - 1
  for j in reversed(range(n)):
    while i < m and matrix[i][j] < b:
      i += 1
    count += m - i

  return count
