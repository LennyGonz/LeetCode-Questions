def num_islands(board):
  num_rows = len(board)
  num_cols = len(board[0])
  count = 0

  visitied = [[False for _ in range(num_cols)] for _ in range(num_rows)]
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == 1 and not visitied[row][col]:
        fill(board, visitied, row, col)
        count += 1
  return count

def fill(board, visitied, row, col):
  moves = [(0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)]
  visitied[row][col] = True

  for move_row, move_col in moves:
    new_row, new_col = (row + move_row, col + move_col)
    if (inside_board(board, new_row, new_col) and board[new_row][new_col] == 1 and not visitied[new_row][new_col]):
      fill(board, visitied, new_row, new_col)

def inside_board(board, row, col):
  return 0 <= row < len(board) and 0 <= col < len(board[0])
