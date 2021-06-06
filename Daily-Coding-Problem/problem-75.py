def longest_increasing_subsequence(arr):
  if not arr:
    return 0
  cache = [1] * len(arr)
  for i in range(1, len(arr)):
    for j in range(i):
      if arr[i] > arr[j]:
        cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)
