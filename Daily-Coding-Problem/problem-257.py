def window(array):
  left, right = None, None
  n = len(array)
  max_seen, min_seen = -float("inf"), float("inf")

  for i in range(n):
    max_seen = max(max_seen, array[i])
    if array[i] < max_seen:
      right = i

  for i in range(n - 1, -1, -1):
    min_seen = min(min_seen, array[i])
    if array[i] > min_seen:
      left = i

  return left, right

'''
This will take two passes over the array, operating in O(N) time and O(1) space.
'''
