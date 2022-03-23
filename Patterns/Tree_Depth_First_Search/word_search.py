'''
LeetCode #79

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

------------------------------------------------------------------------------------------------------------------------------------------------------
There is no super optimal solution so we default to the bruteforce

* We check every single cell for the 1st character of the given word, then the 2nd character and so on

* we're going through every single position in the matrix
  * then checking every single neighbor (to see if it's possible to make our target word)

* DFS is the best approach

To avoid duplicates there are 2 approaches we can take
1) using a set
  - According to Python wiki: Time complexity, set is implemented as a hash table.
  - So you can expect to lookup/insert/delete in O(1) average. Unless your hash table's load factor is too high, then you face collisions and O(n).

Apparently the most optimal way to avoid duplicates is using a binary matrix
* answer is below
'''

def exist(board, word):
  # We want to grab the dimensions of the board
  rows = len(board)
  cols = len(board[0])
  
  # we'll use a set to store the matrix locations of the character's we've visited
  # this will allow us to avoid duplicates
  path = set()
  
  def dfs(r,c,index):
    if index == len(word):
      return True
    
    # the first 4 conditions tell us if we're out of bounds, if we are -> return False
    # if the current character we're on in word IS NOT THE SAME as the character we're on in the matrix -> return False
    # if we've visited the current character in the matrix before -> return false
    # if any of these 6 conditions are true, we want to immediately return False
    if(r < 0 or c < 0 or r >= rows or c >= cols or word[index] != board[r][c] or (r,c) in path):
      return False
    
    # we want to add the current location of the character to our set so we avoid using it, thus no duplicates
    path.add((r,c))
    
    # we recursively run dfs on all 4 adjacent positions: right, left, up, and down
    # if any recursive call return True, then res returns True
    res = (dfs(r+1,c,index+1) or
           dfs(r-1,c,index+1) or
           dfs(r,c+1,index+1) or
           dfs(r,c-1,index+1))
    
    # we remove the last position we were at b/c we're no longer visiting that position
    # we're returning from that function call, therefore we don't need to continue to visit that position inside our path
    path.remove((r,c))
    
    return res

  # we want to go through every position in our board and run dfs on it
  # and if any of our dfs calls return True, we can return True
  for r in range(rows):
    for c in range(cols):
      if dfs(r,c,0):
        return True
  
  return False

def exist2(board, word):
  ROWS = len(board)
  COLS = len(board[0])
  
  booleanMatrix = [[False for x in range(COLS)] for j in range(ROWS)]
  
  def dfs(r,c,i):
    if i == len(word):
      return True
    
    if(r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or booleanMatrix[r][c] == True):
      return False
    
    #path.add((r,c))
    
    res = (dfs(r+1,c,i+1) or
           dfs(r-1,c,i+1) or
           dfs(r,c+1,i+1) or
           dfs(r,c-1,i+1))
    
    #path.remove((r,c))
    return res

  for r in range(ROWS):
    for c in range(COLS):
      if dfs(r,c,0):
        return True
  
  return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(exist(board, word))
print(exist2(board, word))

'''
Time: (N x M x 4^N) -> NxM (dimensions of the board) & we call the dfs function every single time for every position in the board, the call stack for dfs is the len(word), but we have 4 branches of DFS.. so it's 4^(len(word)) ~approx~ 4^N, where N is the length of the word

Space: O(N^2)-> we use a set/matrix
'''
