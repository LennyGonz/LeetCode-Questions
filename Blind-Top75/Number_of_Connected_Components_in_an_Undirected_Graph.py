'''
LeetCode #323

You have a graph of n nodes.

You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

ex: Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

----------------------------------------------------------------------------------------------------------------------------------------

A node by itself counts as a connected component

In an undirected graph, a connected component is a subgraph in which each pair of vertices is connected via a path.
So essentially, all vertices in a connected component are reachable from one another.

1. If we run DFS, starting from a particular vertex, it will continue to visit the vertices depth-wise until 
		there are no more adjacent vertices left to visit. 

2. Thus, it will visit all of the vertices within the connected component that contains the starting vertex. 

3. Each time we finish exploring a connected component, we can find another vertex that has not been visited yet, and start a new DFS from there. 
		The number of times we start a new DFS will be the number of connected components.

So to do this we use the given array: edges to create an adjancency list AND traverse it using dfs

We start dfs on node 0 - mark node 0 as visited, then look at its neighbors

then visit node 1 - mark node 1 as visited, then look at its neighbors

visit node 2 - mark node 2 as visited, look at its neighbors - node 2 has no neighbors so we start dfs on the nodes we HAVENT visited

This approach takes O(E+V) time, because we have to visit every edge and vertex. Same for space bc of the adjacency list
'''
from collections import defaultdict

def countComponents(n, edges):
	graph = defaultdict(list)
	
	# we'll create our adjacency list
	# remember that if we have: [[0,1],[1,2],[3,4]]
	# 0 and 1 are connected both ways - the edges are bidirectional
	# x = 0 and y = 1 [0,1]
	for x, y in edges:
		graph[x].append(y)
		graph[y].append(x)
	# {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]} -> our end adjancency list

	def dfs(node, seen):
		seen.add(node)
		for neighbor in graph[node]:
			if neighbor not in seen:
				dfs(neighbor, seen)

	count = 0
	seen = set()
	for node in range(n):
		if node not in seen:
			dfs(node, seen)
			count += 1
	return count

def countComponents(n, edges):
	par = [i for i in range(n)]
	rank = [1] * n
	
	def find(n1):
		res = n1
		
		while res != par[res]:
			par[res] = par[par[res]]
			res = par[res]

		return res
	
	def union(n1,n2):
		p1, p2 = find(n1), find(n2)
  
		if p1 == p2:
			return 0

		if rank[p2] > rank[p1]:
			par[p1] = p2
			rank[p2] += rank[p1]

		else:
			par[p2] = p1
			rank[p1] += rank[p2]

		return 1

	res = n
	
	for n1, n2 in edges:
		res -= union(n1, n2)
	return res

print(countComponents(5, [[0,1],[1,2],[3,4]]))
