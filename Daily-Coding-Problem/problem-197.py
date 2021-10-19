def reverse(array, left, right):
  while left < right:
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

def rotate(array, k):
  n = len(array)
  reverse(array, 0, n - k - 1)
  reverse(array, n - k, n - 1)
  reverse(array, 0, n - 1)
  return array
