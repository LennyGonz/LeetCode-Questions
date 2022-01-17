def helper(v, visited, stack, edges):
  visited[v] = True

  for neighbor, _ in edges[v]:
    if not visited[neighbor]:
      helper(neighbor, visited, stack, edges)

  stack.append(v)

def toposort(edges, num_vertices):
  visited = [False for _ in range(num_vertices)]
  stack = []

  for v in range(num_vertices):
    if not visited[v]:
      helper(v, visited, stack, edges)

  return stack

# Implemented this way, topological sort will take O(V + E) time.

def get_distances(edges, stack):
  dist = [float('inf') for _ in range(len(stack))]
  dist[0] = 0

  while stack:
    curr = stack.pop()

    for neighbor, distance in edges[curr]:
      if dist[neighbor] > dist[curr] + distance:
        dist[neighbor] = dist[curr] + distance

  return dist[1:]

'''
We must call this method twice: once to compute the shortest paths between the runner's house and any uphill location, and a second time (with reversed edges) to compute the shortest downhill paths between those locations and the runner's house.

Each of these calls will take O(V + E) time, since we must traverse the entire graph in the worst case.

Finally, since we know all the possible ways to get to and from the highest locations, we can sum up each pair of distances and return the minimum overall. The main function will be as follows:
'''
def shortest_route(elevations, paths):
  uphill_edges = defaultdict(list)
  downhill_edges = defaultdict(list)
  all_edges = defaultdict(list)

  for (start, end), distance in paths.items():
    all_edges[start].append((end, distance))
    if elevations[start] < elevations[end]:
      uphill_edges[start].append((end, distance))
    else:
      downhill_edges[end].append((start, distance))

  num_vertices = len(all_edges.keys())
  stack = toposort(all_edges, num_vertices)  

  uphill_distances = get_distances(uphill_edges, list(stack))
  downhill_distances = get_distances(downhill_edges, list(stack))

  return min(x + y for x, y in zip(uphill_distances, downhill_distances))

'''
The total running time of this algorithm will be O(V + E), as this is an upper bound for each of our component functions.
We have used a few extra dictionaries to store the uphill and downhill edges for the sake of clarity, but the space complexity will still be O(V + E).
'''
