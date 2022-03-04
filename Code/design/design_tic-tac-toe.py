'''
LeetCode #348 Design Tic-Tac-Toe - Facebook & Amazon & Microsoft & Apple & Google & Bloomberg & SalesForce

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.


Implement the TicTacToe class:

1. TicTacToe(int n) Initializes the object the size of the board n.
2. int move(int row, int col, int player): Indicates that the player with id player plays at the cell (row, col) of the board.
    The move is guaranteed to be a valid move.

example:

Input: 
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

Output:
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

---------------------------------------------------------
Strategy: 

Let's only look at rows first:

row[] represents the move count of a row
If player1 move on a cell in row[1], then row[1]+=1
If player2 move on a cell in row[1], then row[1]-=1

If both player1 and player2 move on some cells in row[1], then 
  row[1] will never become "n" because it is guaranteed that all moves are valid and will only moves on empty cells.

If row[1] becomes "n", if it is currently player1's move, then player1 wins, else player2 wins.
For each move, only check rows of current move, no need to check all rows.

Do the same for columns to check winning condition on column.

For diagnal, if rowIdx-colIdx==0, that means the move is on top-left to right-bottom diagnal. If rowIdx+colIdx==n, that means the move is on top-right to bottom-left diagnal.

So total space is "rows array + columns array + two diagnals": O(n+n+1+1)==O(n)

For each move, time checking current row, column, and two diagnals takes O(1+1+1+1)==O(1)
'''

class TicTacToe:
  def __init__(self, n: int):
    self.row=[0]*n
    self.col=[0]*n
    self.diag1=0
    self.diag2=0
    self.n=n

  def move(self, row: int, col: int, player: int) -> int:
    self.row[row]+=1 if player==1 else -1
    self.col[col]+=1 if player==1 else -1
    if row+col==self.n-1:
      self.diag1+=1 if player==1 else -1
    if row-col==0:
      self.diag2+=1 if player==1 else -1
    if abs(self.row[row])==self.n or abs(self.col[col])==self.n or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
      return 1 if player==1 else 2
    return 0

'''
Time: O(1)
Space: O(N)
'''
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

'''
Example Testcase:

["TicTacToe","move","move","move","move","move","move","move"]
[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
'''
