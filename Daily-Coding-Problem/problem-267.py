def check(board):
  location = find_king(board)

  pawns = get_pawn_moves(board, location)
  crosses = get_cross_moves(board, location)
  diagonals = get_diagonal_moves(board, location)
  knights = get_knight_moves(board, location)

  if 'P' in pawns or 'B' in diagonals or 'Q' in diagonals or 'R' in crosses or 'Q' in crosses or 'N' in knights:
    return True

  return False

def find_king(board):
  for row in range(8):
    for col in range(8):
      if board[row][col] == 'K':
        return row, col

def get_pawn_moves(board, row, col):
  if row < 6:
    return [board[row + 1][col - 1], board[row + 1][col + 1]]
  else:
    return []

def get_cross_moves(board, row, col):
  pieces = []

  for c in range(col - 1, 0, -1):
    if board[row][c] != '.':
      pieces.append(board[row][c])
      break

  for c in range(col + 1, 8, 1):
    if board[row][c] != '.':
      pieces.append(board[row][c])
      break

  for r in range(row + 1, 8, 1):
    if board[row][c] != '.':
      pieces.append(board[r][col])
      break

  for r in range(row - 1, 0, -1):
    if board[row][c] != '.':
      pieces.append(board[r][col])
      break

  return pieces

def diagonal_moves(board, row, col):
  pieces = []

  for r, c in zip(range(row + 1, 8, 1), range(col + 1, 8, 1)):
    if board[r][c] != '.':
      pieces.append(board[r][c])
      break

  for r, c in zip(range(row + 1, 8, 1), range(col - 1, -1, -1)):
    if board[r][c] != '.':
      pieces.append(board[r][c])
      break

  for r, c in zip(range(row - 1, -1, -1), range(col + 1, 8, 1)):
    if board[r][c] != '.':
      pieces.append(board[r][c])
      break

  for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
    if board[r][c] != '.':
      pieces.append(board[r][c])
      break

  return pieces

def is_legal(row, col):
  return 0 <= row <= 7 and 0 <= col <= 7

def knight_moves(board, row, col):
  moves = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
  destinations = [(row + i, col + j) for (i, j) in moves]
  return [board[row][col] for row, col in destinations if is_legal(row, col)]
