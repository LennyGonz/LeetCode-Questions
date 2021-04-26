def max_subarray_sum(arr):
  max_ending_here = max_so_far = 0
  for x in arr:
    max_ending_here = max(x, max_ending_here + x)
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far

# This algorithm is known as Kadane's algorithm, and it runs in O(N) time and O(1) space.
