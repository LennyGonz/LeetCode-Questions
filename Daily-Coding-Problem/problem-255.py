def helper(reachable, graph, i, j):
  reachable[i][j] = 1

  for v in graph[j]:
    if reachable[i][v] == 0:
      reachable = helper(reachable, graph, i, v)

  return reachable

def closure(graph):
  n = len(graph)
  reachable = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    reachable = helper(reachable, graph, i, i)

  return reachable

'''
The time complexity of depth-first search is O(V + E), so this algorithm will take O(V * (V + E)).
In the case where our graph is maximally dense, E = V2, so this will be similar to above.
'''
