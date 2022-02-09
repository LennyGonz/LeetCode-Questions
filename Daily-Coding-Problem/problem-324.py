def send(mice, holes):
  mice.sort()
  holes.sort()

  moves = 0
  for i in range(len(mice)):
    moves = max(moves, abs(mice[i] - holes[i]))

  return moves
