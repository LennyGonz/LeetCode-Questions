def num_ways(n, m):
  A = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    A[i][0] = 1
  for j in range(m):
    A[0][j] = 1
  for i in range(1, n):
    for j in range(1, m):
      A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[-1][-1]
