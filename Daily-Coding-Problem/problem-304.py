from typing import List, Tuple

def get_moves(position: Tuple[int, int]) -> List[Tuple[int, int]]:
  i, j = position
  moves = [
    (i + 2, j + 1),
    (i + 2, j - 1),
    (i - 2, j + 1),
    (i - 2, j - 1),
    (i + 1, j + 2),
    (i + 1, j - 2),
    (i - 1, j + 2),
    (i - 1, j - 2),
  ]
  return moves

def get_knight_on_board_probability_helper(position: Tuple[int, int], k: int) -> int:
  i, j = position
  if not (0 <= i < 8) or not (0 <= j < 8):
    return 0
  if k == 0:
    return 1
  # generating total number of valid moves from current position
  moves = get_moves(position)
  accumulator = 0
  for pos in moves:
    accumulator += get_knight_on_board_probability_helper(pos, k - 1)
  return accumulator


def get_knight_on_board_probability(position: Tuple[int, int], k: int) -> float:
  # P(knight remains on board) = (number of positions on board / total positions)
  number_of_move_in_board = get_knight_on_board_probability_helper(position, k)
  return number_of_move_in_board / pow(8, k)


if __name__ == "__main__":
  print("{:.3f}".format(get_knight_on_board_probability((4, 4), 1)))
  print("{:.3f}".format(get_knight_on_board_probability((4, 4), 2)))
  print("{:.3f}".format(get_knight_on_board_probability((1, 1), 3)))


"""
SPECS:
TIME COMPLEXITY: O(8 ^ k)
SPACE COMPLEXITY: O(k)
"""

def get_moves(x, y):
  moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
  return [(x + i, y + j) for (i, j) in moves]

'''
With this out of the way, we can formulate a straightforward recursive solution to our problem. There are two base cases:

When we reach the last move, we should return 1 if the knight is still on the board, else 0.
If at any point the knight moves off the board, the probability of that path becomes 0.
Otherwise, we should retrieve all eight jumps that can be made from the current square, apply our function to each of them, and average the results.
'''

def on_board(x, y):
  return 0 <= x <= 7 and 0 <= y <= 7

def get_probability(x, y, k):
  if k == 0:
    return on_board(x, y)
  if not on_board(x, y):
    return 0

  jumps = get_moves(x, y)
  res = [get_probability(x, y, k - 1) for x, y in jumps]

  return 0.125 * sum(res)

def get_probability(x, y, k, memo={}):
  if (x, y, k) in memo:
    return memo[(x, y, k)]

  if k == 0:
    return on_board(x, y)
  if not on_board(x, y):
    return 0

  jumps = get_moves(x, y)
  probs = [get_probability(x, y, k - 1, memo) for x, y in jumps]

  memo[(x, y, k)] = 0.125 * sum(probs)

  return memo[(x, y, k)]
