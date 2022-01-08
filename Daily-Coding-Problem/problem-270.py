from heapq import *

class Network:
  def __init__(self, N, edges):
    self.vertices = range(N + 1)
    self.edges = edges

  def make_graph(self):
    graph = {v: [] for v in network.vertices}

    for u, v, w in network.edges:
      graph[u].append((v, w))

    return graph

def propagate(network):
  graph = network.make_graph()
  times = {}

  q = [(0, 0)]
  while q:
    u, node = heappop(q)
    if node not in times:
      times[node] = u
      for neighbor, v in graph[node]:
        if neighbor not in times:
          heappush(q, (u + v, neighbor))

  return max(times.values())

'''
It takes O(log E) time to pop or push an element from the heap, and we must do this for each edge, so the complexity of this algorithm is O(E log E).
'''
