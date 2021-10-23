def lcs(a, b, c):
  lengths = [[[0 for k in range(len(c) + 1)]
              for j in range(len(b) + 1)]
              for i in range(len(a) + 1)]

  for i, x in enumerate(a):
    for j, y in enumerate(b):
      for k, z in enumerate(c):
        if x == y == z:
          lengths[i + 1][j + 1][k + 1] = lengths[i][j][k] + 1
        else:
          lengths[i + 1][j + 1][k + 1] = max(
                  lengths[i][j + 1][k + 1],
                  lengths[i + 1][j][k + 1],
                  lengths[i + 1][j + 1][k]
                  )

  return lengths[-1][-1][-1]
