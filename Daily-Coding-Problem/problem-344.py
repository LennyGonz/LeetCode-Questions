'''
We now see that 3 still has an odd number of descendants, so we can cut the link between 1 and 3. In total, then, we are able to remove two edges.

It is not necessary, however, to remove the edges precisely in this order.

Instead, it is sufficient to know that this greedy approach works, so that we can identify all the nodes with an odd number of descendants
(except for the root, which cannot be cut off in this way), and increment a counter for each.

Let's assume our input is presented in the form of a graph, like so:
'''
graph = {
  1: [2, 3],
  2: [],
  3: [4, 5],
  4: [6, 7, 8],
  5: [],
  6: [],
  7: [],
  8: []
}

'''
We will first perform a depth-first search traversal through this graph to populate a dictionary which stores the number of descendants per node.
Once this is done, we simply count up how many of these values are odd and return this total.
'''

from collections import defaultdict

def traverse(graph, curr, result):
  descendants = 0

  for child in graph[curr]:
    num_nodes, result = traverse(graph, child, result)

    result[child] += num_nodes - 1
    descendants += num_nodes

  return descendants + 1, result

def max_edges(graph):
  start = list(graph)[0]
  vertices = defaultdict(int)

  _, descendants = traverse(graph, start, vertices)

  return len([val for val in descendants.values() if val % 2 == 1])

# Our tree will have N nodes, so the depth-first search will take O(N) time. 
# The space complexity is likewise O(N), since we populate a dictionary with N keys, one for each node.
