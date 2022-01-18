'''
How do we determine if we're at an island or how do we know if it's the same island ?

* draw out a diagram - starting at the first index [0][0] and visiting the 4 possible neighbors (left, right, up, and down)
* then repeat the same process on EACH neighbor

TO AVOID visiting the same island, we use a set, but we don't put the entire island in there
We put the points/location we've visited in the set

So essentially we start by performing BFS on 1 node and then BFS on its neighbors adding each node to our visited set to keep track

IF we start at [0][0] we need to find out how big the island really is
  * islands are formed by connecting 1s horizontally (left-right) and vertically (up-down)
By checking the 4 possible directions we may find more land that creates the current island

Not only do we do BFS on both recently discovered neighbors but we also need to mark them as visited
  * marking them as visited is cruical bc we'll be exploring every single cell
  * so to avoid revisiting & recounting land as "new" we add each coordinate where we discover land to the set

Thats it

1. We can start by grabbing the dimensions of the input matrix
2. we create out visit set & islands variable (this will serve as our count every time we discover a new island)

3. For every row and column in that - each row if we find a position with land AND we haven't visited that position before then
  - perform BFS on the current position
  - when BFS is done - increment islands by 1
  
  3b) BFS 
    - we create and initialize the queue
    - add the current location to the visited set
    - in the while-loop we grab our current location and calculate the possible directions
      - iterate through all possible positions AND if the position is inbounds of the inputMatrix AND we haven't visited this position
        - then we add this new position to our queue
        - AND add it to the visit set
        - then restart the whole process
'''
from collections import deque

def numIslands(grid):
  if not grid:
    return 0
  
  ROWS, COLS = len(grid), len(grid[0])
  visited = set()
  islands = 0
  
  def bfs(r,c):
    # if we used a list here and use pop instead of pop list
    # this algorithm becomes DFS
    queue = deque([(r,c)])
    visited.add((r,c))
    
    while queue:
      row, col = queue.popleft() # grab our current location in the grid
      directions = [[1,0],[-1,0],[0,1],[0,-1]]    
      
      for rd, cd in directions:
        # we want to check that this position (this being any of the 4 positions in directions) is in bounds
        r, c = row+rd, col + cd
        
        if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited):
          queue.append((r,c))
          visited.add((r,c))
  
  # we want to search every single cell in the matric
  # BUT only do BFS on the cells that are marked as LAND
  # AND cells we havent visited
  for r in range(ROWS):
    for c in range(COLS):
      if(grid[r][c] == "1" and (r,c) not in visited):
        bfs(r,c)
        islands += 1
  
  return islands

'''
Time complexity O(M * N): where M is the number of rows and N is the number of columns.
Space complexity O(M*N): in case that the grid map is filled with lands where BFS goes M*N deep
'''
