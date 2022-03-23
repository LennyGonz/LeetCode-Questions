'''
Leetcode #261

You have a graph of n nodes labeled from 0 to n - 1.

You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
           0
        /  |  \
       1   2   3
       |
       4
Output: true
---------------------------------------------------------------------------------------------------------------------------------------------------------

We start with listing facts we know about Trees

* Trees are not allowed to have loops
* Trees must be connected

Do empty graphs count as acceptable trees?

-> If either of these conditions are violated we can return False

Using the input array: edges -> we'll make an adjacency list

For each node, we want to know what neighbors that node has
  - so we'll create a list of neighbors for EVERY input node

Then we perform our checks to make sure it's a tree

So if we're given a tree like:
           0
        /  |  \
       1   2   3
       |
       4
We'll run dfs starting with node 0
  - we run DFS on every single node and visit its neighbors recursively
    until we visit every single node that's connected to node 0

At the end we'll take the # of input odes we're given (in this example 5) and
then check if the number of visited nodes matches the # of input nodes
  - if they match, every single node in the graph is connected

Then we must check if the graph contains any cycles/loops
  - if we encounter a cycle/loop we return False, otherwise true

* we use a hasSet to keep track of the visited nodes

1) Is there a loop? Not detected while iterating through the graph
2) Are all the nodes connected ?
    - while iterating we kept track of the numbers we've iterated through
      - if that number matches the input value: n
        - then they are connected
      - if that number DOES NOT MATCH the input value
        - then they are NOT connected

Time: O(E+V) - because we have to visit every edge and vertex
Space: O(E+V) - We use an adjacency list
'''

def validTree(n, edges):
  # if we're not given any nodes at all
  if not n:
    # empty graphs count as a tree
    return True
  
  # for every single node in our input (n)
  # I want to create a pair, the value of that node and an empty list
  adj = {i: [] for i in range(n)}
  
  print(adj)
  # then i want to go through every edge (pair of nodes)
  # and starting populating the adjacency list
  for node1, node2 in edges:
    adj[node1].append(node2)
    adj[node2].append(node1)
  print("adj: ", adj)
  # this will keep track of every node we visit
  visited = set()
  
  def dfs(currentNode, previousNode):
    # this will help detect a loop
    # if we visited the currentNode, we're in a loop -> return false
    if currentNode in visited:
      return False
    
    # if it's not in the visit set
    # we mark it as visited
    visited.add(currentNode)
    
    # we go through every neighbor of the currentNode
    for neighbor in adj[currentNode]:
      # if the neighbor is the same as the node we came from, we skip this iteration
      if neighbor == previousNode:
        continue
      
      # if it's NOT the previousNode we came from, we call dfs on that neighbor
      # the previous value will be the currentNode because that's where we're coming from when we arrived at the neighbor
      if not dfs(neighbor, currentNode):
        # if we enter this, we detected a loop
        # if we DONT enter, we just continue traversing all the other neighbors
        return False
    
    # if we go through every single neighbor without returning false
    # then we can return True bc we didn't detect a loop
    return True
  
  # we call our dfs function, starting at node 0, and the previous value is -1 b/c that'll never exist in our graph
  # we must also make sure that the entire graph is connected, so n must equal the length of visited -> bc that means we've visited every node -> which means all the nodes are connected
  return dfs(0,-1) and n == len(visited)

def main():
  n = 5
  edges = [[0,1],[0,2],[0,3],[1,4]]
  print(validTree(n, edges)) # True

main()

