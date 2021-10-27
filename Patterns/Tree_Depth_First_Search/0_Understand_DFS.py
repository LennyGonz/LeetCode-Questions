'''
1. Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
2. Repeat until all the nodes are visited, or the node to be searched is found.

        A
      /   \
     B     C 
    /  \    \
   D    E -> F

*This is a Directed Graph

But keep in mind -> DFS can be implemented using Pre-Order, In-Order, and Post-Order traversal methods

Pre-Order we visit the root node, then travel the left child, then right child

In-Order we visit the left child, then visit the root node, then visit the right child

Post-Order we visit the left subtree, then the right subtree, and then the root node
'''

not_a_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
  if node not in visited:
    print (node)
    visited.add(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)

# Driver Code
#dfs(visited, graph, 'A')

graph = {
  "A":["D","C","B"],
  "B":["E"],
  "C":["G","F"],
  "D":["H"],
  "E":["I"],
  "F":["J"]}

def dfs_non_recursive(graph, node):
  if node is None or node not in graph:
    return "Invalid input"
  
  path = []
  
  stack = [node]
  
  while(len(stack) != 0):
    curr_node = stack.pop()
    
    if curr_node not in path:
      path.append(curr_node)
    
    # for the leaf node cases -> in our graph those would be I, J, G, H
    # If we remove this check, we'll get a KeyError, bc these leaf nodes are not in our graph representation above
    if curr_node not in graph:
      continue
    for neighbor in graph[curr_node]:
      print("neighbor: ", neighbor)
      stack.append(neighbor)

  return " ".join(path)

DFS_path = dfs_non_recursive(graph, "A")

print(DFS_path)
