from collections import defaultdict

def find_component(graph, visited, current_word):
  visited.add(current_word)

  for neighbor in graph[current_word]:
    if neighbor not in visited:
      find_component(graph, visited, neighbor)

  return visited

def is_connected(graph):
  start = list(graph)[0]
  component = find_component(graph, set(), start)

  reversed_graph = defaultdict(list)
  for key, values in graph.items():
    for v in values:
      reversed_graph[v].append(key)
  reversed_component = find_component(graph, set(), start)

  return component == reversed_component == graph.keys()

def are_degrees_equal(graph):
  in_degree = defaultdict(int)
  out_degree = defaultdict(int)

  for key, values in graph.items():
    for v in values:
      out_degree[key] += 1
      in_degree[v] += 1

  return in_degree == out_degree

def make_graph(words):
  graph = defaultdict(list)

  for word in words:
    graph[word[0]].append(word[-1])

  return graph

def can_chain(words):
  graph = make_graph(words)

  degrees_equal = are_degrees_equal(graph)
  connected = is_connected(graph)

  return degrees_equal and connected
