def fixed_point(array):
  low, high = 0, len(array)

  while low <= high:
    mid = (low + high) // 2
    if array[mid] == mid:
      return mid
    elif array[mid] < mid:
      low = mid + 1
    else:
      high = mid - 1

  return False

# The complexity of this solution is the same as that of binary search, O(log N).
