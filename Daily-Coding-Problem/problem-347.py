def bubble_swap(string, i, j):
  string = list(string)

  # Rotate so that i is at the beginning.
  while i > 0:
    string = string[1:] + string[:1]
    i -= 1

  # Move the first two letters to the end in reversed order.
  string = string[:1] + string[2:] + string[1:2]
  string = string[1:] + string[:1]

  # Rotate back to the initial position.
  while len(string) > j + 1:
    string = string[1:] + string[:1]
    j += 1

  return ''.join(string)
'''
As indicated by the name, this operation is exactly that used for bubble sort. Therefore, so long as we are allowed to move either the first or second letter, we can always obtain a fully sorted string.

Our full solution, then, will be to return the alphabetically earliest rotation if k = 1, and otherwise the sorted string.
'''

def get_best_word(string, k):
  string = list(string)

  if k == 1:
    best = string
    for i in range(1, len(string)):
      if string[i:] + string[:i] < best:
        best = string[i:] + string[:i]
    return ''.join(best)

  else:
    return ''.join(sorted(string))

'''
In the first case, our algorithm loops through Nrotations and compares two strings of length N, for a time complexity of O(N^2).
The space required will be O(N), the size of our two string variables.

For the latter, sorting our string will take O(N log N) time, and building the new string will require O(N) space.
'''
