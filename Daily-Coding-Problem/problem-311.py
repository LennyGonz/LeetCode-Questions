def peak(array):
  n = len(array)
  start, end = 0, n - 1

  while start + 1 <= end:
    mid = start + (end - start) // 2

    if array[mid - 1] < array[mid] > array[mid + 1]:
      return array[mid]
    elif array[mid] < array[mid + 1]:
      start = mid + 1
    else:
      end = mid - 1

  return array[start]

'''
Since we are using binary search to search for a peak, this algorithm is logarithmic in the length of the input array.
The space complexity is O(1), since we only need to check values in the input array.
'''
