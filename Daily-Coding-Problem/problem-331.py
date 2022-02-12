def num_flips(string):
  flips = [[0 for _ in range(2)] for _ in range(len(string))]

  for i, char in enumerate(string):
    if char == 'x':
      flips[i][0] = flips[i - 1][0]
      flips[i][1] = min(flips[i - 1]) + 1
    else:
      flips[i][0] = flips[i - 1][0] + 1
      flips[i][1] = min(flips[i - 1])

  return min(flips[-1])

'''
This algorithm iterates over our string in a single pass and requires an array twice the size of our input, so it will run in O(N) time and space.

An alternative solution is as follows. First, we make a pass over our input to determine the number of y's to the left of each element. We then make a second pass to find the number of x's to the right of each element.

For any solution, there must be some element in our string for which everything to its left gets set to x, and everything to its right gets set to y. As a result, we can simply find the pairwise sum of these lists, and use the element which requires the smallest total number of flips.
'''

def num_flips(string):
  n = len(string)
  y_left = [0] * n
  x_right = [0] * n

  l, r = 0, 0
  for i in range(n):
    y_left[i] = l
    if string[i] == 'y':
      l += 1

  for i in range(n - 1, -1, -1):
    x_right[i] = r
    if string[i] == 'x':
      r += 1

  return min(sum(pair) for pair in zip(y_left, x_right))

# This algorithm will run in O(N) space and time as well.
