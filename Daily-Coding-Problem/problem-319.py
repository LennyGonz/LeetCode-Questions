import heapq
from copy import copy

class Board:
  def __init__(self, nums, goal='123456780'):
    self.goal = list(map(int, goal))
    self.tiles = nums
    self.empty = self.tiles.index(0)
    self.original = copy(self.tiles)
    self.heuristic = self.heuristic()

  def __lt__(self, other):
    return self.heuristic < other.heuristic

  def manhattan(self, a, b):
    a_row, a_col = a // 3, a % 3
    b_row, b_col = b // 3, b % 3
    return abs(a_row - b_row) + abs(a_col - b_col)

  def heuristic(self):
    total = 0
    for digit in range(1, 9):
      total += self.manhattan(self.original.index(digit), self.tiles.index(digit))
      total += self.manhattan(self.tiles.index(digit), self.goal.index(digit))
    return total

  def swap(self, empty, diff):
    tiles = copy(self.tiles)
    tiles[empty], tiles[empty + diff] = tiles[empty + diff], tiles[empty]
    return tiles

  def get_moves(self):
    successors = []
    empty = self.empty

    if empty // 3 > 0:
      successors.append((Board(self.swap(empty, -3)), 'D'))
    if empty // 3 < 2:
      successors.append((Board(self.swap(empty, +3)), 'U'))
    if empty % 3 > 0:
      successors.append((Board(self.swap(empty, -1)), 'R'))
    if empty % 3 < 2:
      successors.append((Board(self.swap(empty, +1)), 'L'))

    return successors

def search(start):
  heap = []
  closed = set()
  heapq.heappush(heap, [start.heuristic, 0, start, ''])

  while heap:
    _, moves, board, path = heapq.heappop(heap)
    if board.tiles == board.goal:
      return moves, path

    closed.add(tuple(board.tiles))
    for successor, direction in board.get_moves():
      if tuple(successor.tiles) not in closed:
        item = [moves + 1 + successor.heuristic, moves + 1, successor, path + direction]
        heapq.heappush(heap, item)

  return float('inf'), None

def solve(nums):
  start = Board(nums)
  count, path = search(start)
  return count, path

'''
The running time and space of A* is O(b^d) in the worst case, where b is the average number of successors per state, and d is the length of the shortest path solution. Using our heuristic, however, reduces this considerably.

Finally, we should note that up to now we have assumed that a solution always exists, which in fact is not the case.
To take an example, we will never be able to permute the following grid to our goal state:

1 2 3
4 5 6
8 7 0

In this case, we will end up evaluating every possible permutation of the board reachable from the starting state, which will be around O(N!).
Where N is the number of digits.
'''
