from collections import deque
################
# DFS Approach #
################
def depthSum2(nestedList):
  def dfs(nestedList, depth):
    total = 0
    for nested in nestedList:
      if nested.isInteger():
        total += nested.getInteger() * depth
      else:
        total += dfs(nested.getList(), depth + 1)
    return total

  return dfs(nestedList, 1)

################
# BFS Approach #
################

def depthSum(nestedList):
  queue = deque(nestedList)

  depth = 1
  total = 0

  while len(queue) > 0:
    for _ in range(len(queue)):
      nested = queue.pop()
      if nested.isInteger():
        total += nested.getInteger() * depth
      else:
        queue.extendedleft(nested.getList())
    depth += 1

  return total

print(depthSum2([1, [4, [6]]]))
