def triplet_sums_to_k(arr, k):
  def pair_sums_to_k(arr, k, start):
    lo = start
    hi = len(arr) - 1
    while lo < hi:
      if arr[lo] + arr[hi] == k:
        return True
      elif arr[lo] + arr[hi] < k:
        lo += 1
      else:
        hi -= 1
    return False

  arr.sort()
  for i in range(len(arr) - 2):
    if pair_sums_to_k(arr, k - arr[i], i + 1):
      return True

  return False
