'''
There are 2 main traversal methods for graphs: depth-first search (DFS) and breadth-first search (BFS)

Below is a typical DFS implementation
This is the recursive version
For each vertex we visit, we call our function again on each of its neighbors
'''
def dfs(graph, start, visited=set()):
  visited.add(start)
  for neighbor in graph[start]:
    if neighbor not in visited:
      dfs(graph,start,visited)
  return visited

'''
While DFS uses a set, for BFS we use a queue
For each items that we pop off the queue, we find its unvisied neighbors and add them to the end of the queue
'''

from collections import deque

def BFS(graph,start,visited={}):
  queue = deque([start])

  while queue:
    vertex = queue.popleft()
    visited.add(vertex)
    for neighbor in graph[vertex]:
      if neighbor not in visited:
        queue.append(neighbor)
  
  return visited

###############################################################################
# Both of these algorithms run in O(V+E) time and O(V) space in the worst case
###############################################################################

'''
Given an undirected graph, determine if it contains a cycle
'''

def DFS(graph, vertex, visited, parent):
  # DFS is traversing the graph so whatever vertex was passed - needs to be marked ar True(visited)
  visited[vertex] = True

  for neighbor in graph[vertex]:
    if not visited[neighbor]:
      if DFS(graph, neighbor, visited, vertex):
        return True
    
    elif parent != neighbor:
      return False
  

def has_cycle(graph):
  visited = {v: False for v in graph.keys()}

  for vertex in graph.keys():
    if not visited[vertex]:
      if DFS(graph, vertex, visited, None):
        return True
  
  return False

'''
Time: O(V+E) - since the worst case we will have to traverse all edges of the graph
Space: O(V) - worst case to store the vertices in a given traversal on the stack
'''
