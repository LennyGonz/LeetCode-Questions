from collections import deque

def numIslands(grid):
  if not grid:
    return
  
  rows, cols = len(grid), len(grid[0])
  
  visited = set()
  
  islands = 0
  
  def bfs(r,c):
    queue = deque()
    visited.add((r,c))
    queue.append((r,c))
    
    while queue:
      # grab the current location
      row, col = queue.popleft()
      
      # the 4 directions we check
      directions = [[1,0],[-1,0],[0,1],[0,-1]]
      
      for rd, cd in directions:
        r = row + rd
        c = col + cd
        if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
          queue.append((r,c))
          visited.add((r,c))

  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1" and (r,c) not in visited:
        bfs(r,c)
        islands += 1
  
  return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid)) #3
