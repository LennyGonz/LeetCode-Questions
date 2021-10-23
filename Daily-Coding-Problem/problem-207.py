graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

def helper(graph, start, colors):
  queue = [start]
  colors[start] = 1

  while queue:
    vertex = queue.pop(0)

    for neighbor in graph[vertex]:
      if colors[neighbor] == 0:
        colors[neighbor] = -colors[vertex]
        queue.append(neighbor)
      elif colors[neighbor] == colors[vertex]:
        return False

  return True

def is_bipartite(graph):
  colors = [0 for _ in range(len(graph))]
  for vertex in graph.keys():
    if colors[vertex] == 0:
      if not helper(graph, vertex, colors):
        return False

  return True
