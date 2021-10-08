def distinct_subarray(arr):
  d = {} # most recent occurrences of each element

  result = 0
  longest_distinct_subarray_start_index = 0
  for i, e in enumerate(arr):
    if e in d:
      # If d[e] appears in the middle of the current longest distinct subarray
      if d[e] >= longest_distinct_subarray_start_index:
        result = max(result, i - longest_distinct_subarray_start_index)
        longest_distinct_subarray_start_index = d[e] + 1
    d[e] = i

  return max(result, len(arr) - longest_distinct_subarray_start_index)

print(distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1]))

# Sliding Window Approach
def longest_subarray_with_distinct_elements(arr):
  window_start = 0
  max_length = 0
  element_map = {}

  for window_end in range(len(arr)):
    right_elem = arr[window_end]

    if right_elem in element_map:
      window_start = max(window_start, element_map[right_elem]+1)
    
    element_map[right_elem] = window_end

    max_length = max(max_length, window_end-window_start+1)
  
  return max_length

print(longest_subarray_with_distinct_elements([5, 1, 3, 5, 2, 3, 4, 1]))
