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
