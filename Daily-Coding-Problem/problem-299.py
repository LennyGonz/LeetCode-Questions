import heapq

def min_spanning_tree(pipes):
  heap = [(0, ('plant', 'plant'))]
  costs = {}; prev = {}

  seen = set()
  vertices = pipes.keys()

  while len(seen) != len(vertices):
    cost, edge = heapq.heappop(heap)
    u, v = edge

    if v not in seen:
      if cost < costs.get(v, float('inf')):
        costs[v] = cost
        prev[v] = u

      for neighbor, cost in pipes[v].items():
        heapq.heappush(heap, (cost, (v, neighbor)))

      seen.add(v)

  path = {v: [] for v in vertices}
  for u, v in prev.items():
    path[v].append(u)

  return path, sum(costs.values())

'''
In the worst case we will need to add and remove each edge to our heap. 
Since each of these operations is O(log N), the overall time and space complexity will be O(N log N), where N is the number of pipes.
'''
