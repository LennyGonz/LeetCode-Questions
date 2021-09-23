def rotate_matrix(matrix):
  n = len(matrix)

  for i in range(n // 2):
    for j in range(i, n - i - 1):
      p1 = matrix[i][j]
      p2 = matrix[j][n - i - 1]
      p3 = matrix[n - i - 1][n - j - 1]
      p4 = matrix[n - j - 1][i]

      matrix[j][n - i - 1] = p1
      matrix[n - i - 1][n - j - 1] = p2
      matrix[n - j - 1][i] = p3
      matrix[i][j] = p4

  return matrix
