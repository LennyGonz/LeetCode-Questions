from collections import defaultdict

def dfs1(node, graph, visited, order):
  visited.add(node)

  for next_node in graph.get(node, []):
    if next_node not in visited:
      dfs1(next_node, graph, visited, order)

  order.append(node)

def toposort(graph):
  order = [] 
  visited = set()

  for node in graph: 
    if node not in visited: 
      dfs1(node, graph, visited, order) 

  return reversed(order)

def get_transpose(graph):
    transpose = defaultdict(list)

    for key, values in graph.items():
        for v in values:
            transpose[v].append(key)

    return transpose

def dfs2(node, graph, visited, components, i):
    visited.add(node)

    components[node] = i

    for next_node in graph.get(node, []):
      if next_node not in components:
        dfs2(next_node, graph, visited, components, i)

def get_connected_components(graph, order): 
  transpose = get_transpose(graph)
  visited = set()
  components = defaultdict(list)
  i = -1

  for i, node in enumerate(reversed(order)):
    if node not in visited:
      dfs2(node, transpose, visited, components, i)

  return components

def negate(x):
  if x[0] == '¬':
    return x[1:]
  else:
    return '¬' + x

def satisfy(variables, *args):
  graph = defaultdict(list)

  for a, b in args:
    graph[negate(a)].append(b)
    graph[negate(b)].append(a)

  order = toposort(dict(graph))
  transpose = get_transpose(graph)
  components = get_connected_components(transpose, order)

  if any(components[v] == components[negate(v)] for v in variables):
    return False
  else:
    return set([max(v, negate(v), key=lambda x: components[x]) for v in variables])

'''
Topologically ordering the graph and finding the strongly connected components both rely on depth-first search, which takes O(V + E) time.

Since neither the number of vertices nor the number of edges is greater than O(N), where N is the number of input clauses, this algorithm will take O(N) time to run overall.

The graph and its transpose will each need to store all variables as keys, so we will require O(N) space as well.
'''
