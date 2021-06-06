VISITED = 0
UNVISITED = 1
VISITING = 2

def max_path(s, lst):
  adj = [[] for v in s]
  # Build adjacency list
  for u, v in lst:
    adj[u].append(v)

  # Create matrix cache
  dp = [[0 for _ in range(26)] for _ in range(len(s))]
  state = {v: UNVISITED for v in range(len(s))}

  def dfs(v):
    state[v] = VISITING
    for neighbour in adj[v]:
      if state[neighbour] == VISITING:
        # We have a cycle
        return True
      dfs(neighbour)
      for i in range(26):
        dp[v][i] = dp[neighbour][i]
    current_char = ord(s[v]) - ord('A')
    dp[v][current_char] += 1
    state[v] = VISITED

    # Run DFS on graph
    for v in range(len(s)):
      if state[v] == UNVISITED:
        has_cycle = dfs(v)
        if has_cycle:
          return None

    return max(max(v for v in node) for node in dp)
