from collections import deque

def minimum_turns(board):
  start, end = 0, 100
  turns = 0
  path = deque([(start, turns)])
  visited = set()

  while path:
    square, turns = path.popleft()

    for move in range(square + 1, square + 7):
      if move >= end:
        return turns + 1

      if move not in visited:
        visited.add(move)
        path.append((board[move], turns + 1))

assert minimum_turns(board) == 7
