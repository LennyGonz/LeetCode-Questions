def valid_playlists(n, m, b):
  ways = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
  ways[0][0] = 1

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      ways[i][j] = ways[i - 1][j - 1] * (m - (j - 1)) + ways[i - 1][j] * max(j - b, 0)

  return ways[n][m]

'''
The time and space complexity of this algorithm will be O(M * N), since we must loop through each cell of our M x N matrix and perform a few calculations.
'''
