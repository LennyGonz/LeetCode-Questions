# Backtracking

Backtracking is an effective technique for solving algorthmic problems

In backtacking, we search depth-first for solutions, backtracking to the **last valid path** as soon as we hit a dead end.

Backtracking reduces the search space since we no longer have to follow down any paths we know are invalid.
This is **called pruning**.

<br>

We must be able to test partial solutions: for example, we can't find a global optimum using backtracking, since we have no idea if the solution we're currently on can lead to it or not.
**But** we can, for example, solve Sudoku using backtracking. We can know immediately if our solution so far is invalid by testing if two of the same number appear in the same row, column, or square.

Let's go through several examples of problems that can be nicely solved with backtracking to drill this concept down.

## 1. The N queens puzzle

The N queens puzzle is the classic backtracking problem. The question is this:

You have an `N by N` board. Write a function that returns the number of possible arrangemens of the board where N queens can be placed oon the board without threatening each other, *i.e. no two queens share the same row,column, or diagonal*

First off, lets describe the brute force solution to this problem, which means trying every single combination of N queens in each of `N*N` spots.
That's $n^2$ choose n. We can immediately improve the runtime of this algorithm by noticing that there's no point in ever placing two queens on the same row (or column), so we really only need to have one queen per row. Now, using brute force, we need to iterate over each row and over each spot on each row. Since we have N rows and N columns, our runtime will be O($n^n$). That's still very slow

It's helpful to ask ourselves three questions to determine whether we can apply backtracking to a problem.

*Can we construct a partial solution*

Yes, we can tentatively place queens on the board

*Can we verify if the partial solution is invalid?*

Yes, we can check a solution is invalid if two queens threaten each other.
To speed this up, we can assume that all queens already placed so far do not threaten each other, so we only need to check if the last queen we added attacks any other queen

*Can we verify if the solution is complete?*

Yes, we know a solution is complete if all N queens have been placed.

Now that we are confident that we can use backtracking, let's apply it to this problem.
We'll loop through the first row and try placing a queen in column 0...N, and then the second, and so on up until N.
What differs here from brute force is that we'll be adding the queens incrementally instead of all at once.

We'll create an `is_valid` function that will check the board on each incremental addition.
`is_valid` will look at the last queen palced and see if any other queen can threaten it. 
If so, then we prune the branch since there's no point pursuing it. Otherwise, we'll recursively call ourselves with the new incremental solution
We only stop once we hit the base case: we've placed all queens on the board already

We can represent our board as just a 1D array of integers from 1...N,
where the value at the index `i` that represents the column the queen on row `i` is on
Since we're working incrementally, we don't even need to have the whole board initialized. We can just append and pop as we go down the stack

```py
def n_queens(n, board=[]):
  if n == len(board):
    return 1
  
  count = 0

  for col in range(n):
    board.append(col)
    if is_valid(board):
      count += n_queens(n, board)
    board.pop()
  return count

def is_valid(board):
  current_queen_row, current_queen_col = len(board) - 1, board[-1]

  # Check if any queens can attack the last queen
  for row, col in enumerate(board[:-1]):
    diff = abs(current_queen_col - col)
    if diff == 0 or diff == current_queen_row - row:
      return False
  return True

```

Let's try it out:

```py 
for i in range(10):
  print(n_queens(i))

# 1
# 1
# 0
# 0
# 2
# 10
# 4
# 40
# 92
# 352
