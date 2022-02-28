import heapq

from collections import defaultdict
from copy import copy

def get_itinerary(flights, source, destination, k):
  costs = defaultdict(lambda: float('inf'))
  costs[source] = 0

  prevs = {}

  for _ in range(k + 1):
    new_costs = copy(costs)

    for u, v, cost in flights:
      if costs[u] + cost < new_costs[v]:
        new_costs[v] = costs[u] + cost
        prevs[v] = u

    costs = new_costs

  if costs[destination] == float('inf'):
    return -1
  else:
    path = [destination]

    while path[-1] != source:
      path.append(prevs[path[-1]])
    path.reverse()

    return costs[destination], path

'''
Since we run k loops, each of which iterates over the list of N input flights, this algorithm will take O(N * k) time.
The space required will be O(V), since at any given time we store a constant number of dictionaries with the different airports as keys.
'''
