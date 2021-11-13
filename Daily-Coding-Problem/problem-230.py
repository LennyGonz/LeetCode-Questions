def min_drops(eggs, floors):
  trials = [[float("inf") for _ in range(floors + 1)] for _ in range(eggs + 1)]

  for i in range(eggs + 1):
    trials[i][0] = 0

  for i in range(1, eggs + 1):
    for j in range(1, floors + 1):
      trials[i][j] = 1 + min([max(trials[i - 1][x - 1], trials[i][j - x]) for x in range(1, j + 1)])

  return trials[eggs][floors]
