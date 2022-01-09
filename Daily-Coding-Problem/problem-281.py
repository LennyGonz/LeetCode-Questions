from collections import defaultdict

def fewest_cuts(wall):
  cuts = defaultdict(int)

  for row in wall:
    length = 0
    for brick in row[:-1]:
      length += brick
      cuts[length] += 1

  return len(wall) - max(cuts.values())

'''
For each brick, we only need to update our dictionary once, so this algorithm will take O(N) time.
Our map will require O(M) space to store a value for each possible edge.
'''
