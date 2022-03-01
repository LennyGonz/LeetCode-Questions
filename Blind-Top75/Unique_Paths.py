'''
Leetcode #62

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).

The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

ex) Input: m = 3, n = 7
    Output: 28

------------------------------------------------------------------------------------------------

This is very much a math problem

We can start with the base case being - just the finish grid

How many ways can you arrive to the finish grid? 1 -> it's itself

So from that we determine the value of each grid to be the number of down+right moves it takes to reach the finish grid

| 2 | 1 |
|---|---|
| 1 |END|

* notice that the grids that have a 1 value have 1s because there is only 1 move possible to arrive at finish
* the grid that has a value of 2 is bc you can either go (down + right = 1) OR (right + down = 1) => 2 distinct paths hence the 2 value

So what we can say is the bottom row will always be 1s because there's only 1 move to make (go right)
The last column will always be 1s because there's only 1 move to make (go down)

Therefore, as we iterate through the rows, we calculate that possible moves from each grid
Since the input is just the grid dimensions, we'll calculate the moves per grid by creating the grid

ex) m = 3, n = 7

start(28)   21  15  10  6  3   1
  7         6   5   4   3  2   1
  1         1   1   1   1  1  END(1)

^ this is what we're trying to achieve
'''
def uniquePaths(m, n):
  # as we discovered the bottom row will always be 1
  row = [1] * n
  
  # since we don't need to calculate the grid movements for the bottom row
  # we only iterate over m-1
  for i in range(m - 1):
    newRow = [1] * n
    
    # we're going to be moving right to left (bc we know the last column is also going to be all 1s)
    # so we START at the 2nd to last column and end at the first column - range(start,stop,step)
    for j in range(n-2, -1, -1):
      # we're creating a new row
      # so we add the left and right value
      newRow[j] = newRow[j+1] + row[j]
    
    # since we're done creating the newRow - to properly calculate the next row
    # we update row to be newRow
    row = newRow
  
  return row[0]

'''
Time: O(MxN) - we create an m x n matrix
Space: O(N) - because that's the length of the row
'''
