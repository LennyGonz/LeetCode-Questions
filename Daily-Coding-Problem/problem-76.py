def bad_cols(board):
  num_bad_cols = 0
  num_cols = len(board[0])
  i = 0
  while i < num_cols:
    if is_sorted_up_to(board, i):
      i += 1
      continue
    else:
      remove_col(board, i)
      num_bad_cols += 1
      num_cols -= 1

  return num_bad_cols

def remove_col(board, i):
  for row in board:
    row.pop(i)

def is_sorted_up_to(board, i):
  '''Returns whether the table is sorted in lexicographic order up to column i.'''
  return all(board[r][:i + 1] <= board[r + 1][:i + 1] for r in range(len(board) - 1))
