class DisjointSet:
  def __init__(self, n):
    self.parents = [i for i in range(n)]
    self.sizes = [1] * n

  def find(self, v):
    root = v
    while root != self.parents[root]:
      root = self.parents[root]

    step = v
    while step != root:
      step, self.parents[step] = self.parents[step], root
    return root

  def join(self, v1, v2):
    s1 = self.find(v1)
    s2 = self.find(v2)

    small, big = (s1, s2) if self.sizes[s1] < self.sizes[s2] else (s2, s1)
    self.parents[small] = big
    self.sizes[big] += self.sizes[small]

def max_spanning_tree(graph):
  """
  Keep adding edges of maximal weight if they join together disjoint sets of vertices.
  Graph is a dict containing a list of vertices and a list of (v1, v2, weight) edges.
  """
  tree = set()
  n = len(graph['vertices'])
  ds = DisjointSet(n)
  graph['edges'].sort(key=lambda x: x[2], reverse=True)

  for edge in graph['edges']:
    if ds.find(edge[0]) != ds.find(edge[1]):
      tree.add(edge)
      ds.join(edge[0], edge[1])

  return tree if len(tree) == n - 1 else None
