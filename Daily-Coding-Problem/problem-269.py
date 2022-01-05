def get_boundaries(dominoes):
  boundaries = []

  low = high = 0
  for high, tile in enumerate(dominoes[1:], 1):
    if tile != '.':
      boundaries.append((low, high))
      low = high

  if boundaries[-1][-1] != len(dominoes) - 1:
    boundaries.append((low, high))

  return boundaries

'''
This will take O(N) time and space, since we must iterate over all dominoes and create a new list that may include every tile.

Once we have these boundaries, we can update the values of the tiles within each section. There are four cases we need to check:

If the section begins at the left edge and goes to an L, the dominoes will all fall left.
If the section begins with an R and goes to the right edge, the dominoes will all fall right.
If the section begins and ends with the same value, all the dominoes in between should fall in that direction.
If the section begins with an R and ends with an L, the tiles in between should fall towards the center.
'''

def push(dominoes):
  boundaries = get_boundaries(dominoes)
  dominoes = list(dominoes)

  for low, high in boundaries:
    if dominoes[low] == '.' and dominoes[high] == 'L':
      dominoes[low : high] = ['L'] * (high - low)

    elif dominoes[low] == 'R' and dominoes[high] == '.':
      dominoes[low : high + 1] = ['R'] * (high + 1 - low)

    elif dominoes[low] == dominoes[high]:
      dominoes[low : high] = dominoes[low] * (high - low)

    elif dominoes[low] == 'R' and dominoes[high] == 'L':
      while low + 1 < high - 1:
        dominoes[low + 1] = dominoes[low]
        dominoes[high - 1] = dominoes[high]
        low += 1; high -= 1
      while low + 1 < high - 1:
        dominoes[low + 1] = dominoes[low]
        dominoes[high - 1] = dominoes[high]
        low += 1; high -= 1
  return ''.join(dominoes)
