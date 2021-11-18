from collections import defaultdict

class Graph:
  # Constructor
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.vertices = vertices
    
  def addEdge(self, u, v):
    self.graph[u].append(v) 

def helperFunction(myGraph, currentNode, visited, result) :
  visited[currentNode] = True # Mark the current node as visited
  print("currentNode in helperFunction: ", currentNode)
  # Recur for all the adjacent vertices of currentNode
  print("myGraph.graph[currentNode]: ", myGraph.graph[currentNode])
  for i in myGraph.graph[currentNode]:
    print("i: ", i, " myGraph.graph[currentNode]: ",  myGraph.graph[currentNode], " currentNode:", currentNode)
    if visited[i] == False :
      helperFunction(myGraph, i, visited, result)
  
  print("currentNode:", currentNode," myGraph.graph outside-for: ", myGraph.graph[currentNode], " result: ", result)
  result.insert(0, currentNode) # Push current vertex to result
  
  
def topologicalSort(myGraph) :
  visited = [False] * myGraph.vertices  # Mark all the vertices as not visited
  print("visited: ", visited)

  result = [] # Our stack to store the result/output
  print("myGraph.vertices: ", myGraph.vertices)
  for currentNode in range(myGraph.vertices):
    print("currentNode: ", currentNode)
    if visited[currentNode] == False:
      helperFunction(myGraph, currentNode, visited, result)

  return(result)


# Driver code 
# Create a graph given in the above diagram 
myGraph = Graph(5) 
myGraph.addEdge(0, 1) # edge from u to v - 0 -> 1
myGraph.addEdge(0, 3) # 0 -> 3
myGraph.addEdge(1, 2) # 1 -> 2
myGraph.addEdge(2, 3) # 2 -> 3
myGraph.addEdge(2, 4) # 2 -> 4
myGraph.addEdge(3, 4) # 3 -> 4

print("Topological Sort")
print(topologicalSort(myGraph))
