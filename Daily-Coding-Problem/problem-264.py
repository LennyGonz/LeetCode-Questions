from itertools import product

def make_graph(C, k):
  vertices = product(C, repeat=k-1)

  edges = {}
  for v in vertices:
    edges[v] = [v[1:] + (char,) for char in C]

  return edges

'''
{'00': ['00', '01']
 '01': ['10', '11']
 '10': ['00', '01']
 '11': ['10', '11']}
'''

def find_eulerian_cycle(graph):
  cycle = []
  start = list(graph)[0]
  before = after = []

  while graph:
    if cycle:
      start = next(vertex for vertex in cycle if vertex in graph)
      index = cycle.index(start)
      before = cycle[:index]; after = cycle[index + 1:]

    cycle = [start]
    prev = start

    while True:
      curr = graph[prev].pop()
      if not graph[prev]:
        graph.pop(prev)

      cycle.append(curr)
      if curr == start:
        break

      prev = curr

    cycle = before + cycle + after

  return cycle

def debruijn(C, k):
  graph = make_graph(C, k)

  cycle = find_eulerian_cycle(graph)

  sequence = [v[-1] for v in cycle[:-1]]

  return sequence
