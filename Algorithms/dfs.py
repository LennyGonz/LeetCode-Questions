'''
Time: O(V + E)

Since ALL the nodes and verticies are visited (worst case), the average time complexity for DFS on a graph is O(V + E)
where V is the number of vertices and E is the number of edges

In case of DFS on a tree:
Time complexity: O(V)

Where V is the number of nodes

* I say average time complexity because a set's `in` operation has an average time complexity of O(1)
If we used a LIST instead, the complexity would be higher!!!!

-- So a set should be used cautiously
'''

graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : [] 
}

visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):
  if node not in visited:
    print("node:", node)
    visited.add(node)
    for neighbor in graph[node]:
      print("neighbor:",neighbor)
      dfs(visited, graph, neighbor)

dfs(visited, graph, 'A')
