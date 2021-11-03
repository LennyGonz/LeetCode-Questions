from collections import defaultdict

def reverse(graph):
  transpose = defaultdict(list)

  for node in graph:
    for neighbor, weight in graph[node]:
      transpose[neighbor].append((node, weight))

  return transpose
