def tilings(n):
  f = [0] * (n + 1)
  g = [0] * (n + 1)

  f[1] = 1; f[2] = 2
  g[1] = 1; g[2] = 2

  for i in range(3, n + 1):
    f[i] = f[i - 1] + f[i - 2] + 2 * g[i - 2]
    g[i] = g[i - 1] + f[i - 1]

  return f[n]
'''
Since we only require a single pass through each array to populate them based on previous values,
the time and space complexity of this algorithm will be O(N).
'''
