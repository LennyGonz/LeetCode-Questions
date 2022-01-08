def throw_dice(n, faces, total):
  ways = [[0 for _ in range(total + 1)] for _ in range(n)]

  for t in range(1, total + 1):
    ways[0][t] = 1 if t <= faces else 0

  for dice in range(1, n):
    for t in range(1, total + 1):
      for face in range(1, min(t, faces + 1)):
        ways[dice][t] += ways[dice - 1][t - face]

  return ways[-1][-1]

'''
Since we must loop through each die, each total, and each face value, the time and space complexity will be O(N * M * T).
'''
