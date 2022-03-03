'''
LeetCode #723

This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy.
A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move.
Now, you need to restore the board to a stable state by crushing candies according to the following rules:

1. If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.

2. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.

3. After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.

4. If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.


You need to perform the above rules until the board becomes stable, then return the stable board.

---------------------------------------------------------------------------------------------------------------------------------------------------
- so what immediately what im trying to figure out is:
  - how am i going to crush the candies
  - how am i going to shift the non-crushed candies DOWN

Crushing Step
When crushing, ONE difficulty is that we might accidentally crush candy that is part of another row. For example, if the board is:

123
145
111

and we crush the vertical row of 1s early, we may not see there was also a horizontal row.

Shifting Step ~~ still not sure
---------------------------------------------------------------------------------------------------------------------------------------------------
A key insight to the problem is to know that IN ORDER TO MAKE CRUSHING CANDIES EASIER
  - we store the locations of the board where a candy can be crushed in a separate data structure
  - we'll use a set as the data structure b/c what we're storing is coordinates and we dont want to crush the same candies

5 Main Steps

1. Mark where the candies can be crushed horizontally
    - loop through the board and check 3 spots AT A TIME to see if there is the same character and that character IS NOT 0

2. Mark where the candies can be crushed vertically
    - loop through the board and check 3 spots AT A TIME to see if there is the same character and that character IS NOT 0

3. Crush the candies
    - go through the set of crushable locations, and EDIT the original board

4. Shift the candies down IF THERE ARE ZEROS BELOW THEM
    - Pay attention to the columns.
    - We will start from the bottom of the board, and work our way up
      - shifting the candies that were not crushed into their "fallen" position

5. Find out where to determine whether or not a board's candies can be crushed anymore
    - If we loop through the entire board, and no candy was crushed, then we are finisheds

Time: O((m*n)^2) where m = rows and n = cols OR you could say O(n) where n is every element in the board => we must loop through the entire board no matter what => and in the worse case the entire board is crushable meaning we'll have to iterate through the entirety of the board twice
Space: O(n) where n is the total number of elements in the board - in the worst case we store the locations of every spot on the board in the set

ex)
[110,005,112,113,114],
[210,211,005,213,214],
[310,311,003,313,314],
[410,411,412,005,414], 
[005,001,512,003,003], ---------> the 2 nested for-loops   -----> crushables = {(6, 2), (8, 4), (7, 1), (8, 1), (6, 1), (8, 3), (7, 2), (8, 2), (9, 1)}
[610,004,001,613,614], ---------> will populate crushables -----> These are the 3 in row (both vertical and horizontal) available
[710,001,002,713,714], ---------> if POSSIBLE              -----> in the initial state of the board
[810,001,002,001,001],
[001,001,002,002,002],
[004,001,004,04,1014]

Next we replace all the 3s in a row with 0s

     0   1   2   3   4
0  [110,005,112,113,114],
1  [210,211,005,213,214],
2  [310,311,003,313,314],
3  [410,411,412,005,414], 
4  [005,001,512,003,003], ---------> Then at step 4, we begin at [9][0] and work our way up, then the next column
5  [610,004,001,613,614], ---------> When we reach a grid where there are ***s we increase the offset, which will be used to move the [5][1] down to [9][1]
6  [710,***,***,713,714], ---------> We do that process until every number has "fallen"
7  [810,***,***,001,001],
8  [001,***,***,***,***],
9  [004,***,004,04,1014]

     0   1   2   3   4
0  [110,005,112,113,114],                                                          [110,000,000,000,000]                                                      
1  [210,211,005,113,114],                                                          [210,000,000,113,114]    
2  [310,311,003,213,214],                                                          [310,000,000,213,214]                                                     
3  [410,411,112,313,314],                                                          [410,000,112,313,314]          
4  [005,005,005,005,414], ----> Then at the end of step 4, we bring down the 0s -> [005,005,005,005,414]
5  [610,211,003,003,003], ---->            this is the end of the 1st iteration -> [610,211,003,003,003]
6  [710,311,412,613,614], ---->            then we repeat the process           -> [710,311,412,613,614]
7  [810,411,512,713,714],                                                          [810,411,512,713,714]
8  [001,001,001,001,001],                                                          [001,001,001,001,001]
9  [004,004,004,04,1014]                                                           [004,004,004,04,1014]
'''

def candyCrush(board):
  ROWS = len(board)
  COLS = len(board[0])
  
  # one iteration of the while loop will
  # find all the candies that are 3 in rows (vertically or horizontally)
  # if there are none - we can exit immediately
  # if there are we place 0s in all the cells where there was a candy that we crushed
  # THEN we start iterating column to column (left to right) moving bottom up -> counting the grids where we crushed a candy (store that number in offset)
  # then we use that offset to determine the coordinate of the the nearest 0 and let the number fall down to where 0 is 
  # NOW we continue using offset to let the 0s fall down and replace the numbers that fell down previously
  while True:
    # this will store the locations of the board where a candy can be crushed
    # each iteration crushables will possibily be populated with new coordinates
    crushable = set()
    
    # step 1 - check for horizontal crushables
    for row in range(ROWS):
      for col in range(COLS-2):
        # 3 consecutive values must be the same AND they cannot be 0
        # in order to be added to crushables bc its candy that can be crushed
        if board[row][col] == board[row][col+1] == board[row][col+2] != 0:
          # update allows me to add 3 coordinates together, rather than 3 add statements
          crushable.update([(row,col),(row,col+1),(row,col+2)])
    
    # step 2 - check for vertical crushables
    for row in range(ROWS-2):
      for col in range(COLS):
        if board[row][col] == board[row+1][col] == board[row+2][col] != 0:
          crushable.update([(row,col),(row+1,col),(row+2,col)])

    # step 5 - if crushable is empty that means there no candies that can be crushed
    if not crushable:
      # so we're done
      return board

    # step 3 - if we haven't returned the board -> that means there ARE candies to crush
    for row,col in crushable:
      # this is how we "crush" the candy
      # every grid we found has the same type as 2+ more grids
      # so we go to every single one of those grids an replace the value with a 0
      board[row][col] = 0
    
    # step 4 - shift the candies down ("falling effect")
    for col in range(COLS):
      offset = 0
      
      # loop through column backward
      for row in range(ROWS-1, -1, -1):
        # we need to know how many rows down a value has to go
        # row will be the last row-cell where a uncrushed candy is
        # offset will be an integer of how many candies were crushed before this current point
        # so K - will tell us how many rows down we have to fall
        k = row + offset
        
        # if this grid-coordinate is in crushable - a candy used to be here 
        # so we increase offset
        if (row,col) in crushable:
          offset += 1
        else:
          # this grid-coordinate is of a candy that was not crushed and needs to fall down to the correct position
          # so we go to the correct row-cell and reassign the value *mimicking the falling effect*
          board[k][col] = board[row][col]
      
      # now that all items have been copied to their right spots
      # place zero's appropriately at the top of the board
      for row in range(offset):
        board[row][col] = 0

def main():
  board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
  print(candyCrush(board)) # [[1, 3, 0, 0, 0], [3, 4, 0, 5, 2], [3, 2, 0, 3, 1], [2, 4, 0, 5, 2], [1, 4, 3, 1, 1]]

  board2 = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
  print(candyCrush(board2))

main()
