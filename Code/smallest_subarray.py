def smallest_subarray_with_given_sum(target, arr):
  window_sum = 0
  min_length = float('inf')
  window_start = 0

  for window_end in range(len(arr)):
    
    window_sum += arr[window_end]

    while window_sum >= target:
      min_length = min(min_length, window_end-window_start+1)
      window_sum -= arr[window_start]
      window_start += 1
    
  if min_length == float('inf'):
    return 0
  
  return min_length

print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))

# import math



# print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))
