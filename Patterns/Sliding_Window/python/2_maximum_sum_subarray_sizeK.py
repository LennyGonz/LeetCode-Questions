'''
Similar to LC #325 - https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

With the sliding window we need to be aware of our window
so we start with: window_start -> this helps me keep track of the beginning of the window & the first element of the window (we adjust this when we need to)

a mini objective is finding the condition for when we stop adding elements together and adjust the window
So we SHOULD focus on the indices of the array, and we can do that by using range(len(arr))

So the variable can be window_end, it'll continuously move until we reach the end of the array

Therefore, we can do window_end >= k-1 *remember arrays have 0-based indices so we account for this offset by doing "-1"
but this condition basically means, once the window_end hits the given size of the window (1) stop record the max_sum (2) adjust the window_sum by subtracting the first element in the window (3) adjust the beginning of the window and slide it to the right by 1 (4) restart everything

Keep this going until we reach the end of the array
'''

def max_sub_array_of_size_k(k, arr):
  window_start = 0
  window_sum = 0
  max_sum = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      # once we've recorded the max (between max_sum and window_sum) now we subtract the first element of the window
      # this allows us to utilize the sum of the previous subarray
      window_sum -= arr[window_start]
      window_start += 1
  return max_sum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))

'''
Time: O(n)
Space: O(1)
'''

'''
1st iteration
window_start = 0
window_sum = 0
max_sum = 0

# [2, 1, 5, 1, 3, 2] -> len(arr) = 6

  for window_end in range(len(arr)):

    # window_end = 0

    window_sum += arr[window_end] -> arr[0] -> 2
    0 += 2
    window_sum = 2

    # 0 >= k-1
    # 0 >= 3-1
    # 0 >= 2
    if window_end >= k-1:
      # false
  
  # for-loop keeps going
  for window_end in range(len(arr)):
    # window_end = 1

    window_sum += arr[window_end] -> 2 += arr[1] -> 2 += 1 -> 3
    window_sum = 3

    # 1 >= k-1
    # 1 >= 3-1
    # 1 >= 2
    if window_end >= k-1:
      #false
  
  # for-loop keeps going
  for window_end in range(len(arr)):
    # window_end = 2

    window_sum += arr[window_end] -> 3 += arr[2] -> 3 += 5 -> 8
    window_sum = 8

    # 2 >= k-1
    # 2 >= 3-1
    # 2 >= 2
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum) -> max(0, 8) -> max_sum = 8
      window_sum -= arr[window_start] -> 8 -= arr[window_start] -> 8 -= arr[0] -> 8 -= 2 -> window_sum = 6
      window_start += 1 -> 0 += 1 -> window_start = 1
  
  2nd iteration
  # [2, 1, 5, 1, 3, 2] -> len(arr) = 6

  for window_end in range(len(arr)):
    # window_end = 3

    window_sum += arr[window_end] -> 6 += 1 -> window_sum = 7
    window_sum = 7

    # 3 >= k-1
    # 3 >= 3-1
    # 3 >= 2
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum) -> max(8,7) -> max_sum = 8
      window_sum -= arr[window_start] -> 7 -= arr[1] -> 7 -= 1 -> window_sum = 6
      window_start += 1
  
  3rd iteration
  # [2, 1, 5, 1, 3, 2] -> len(arr) = 6 
  
  for window_end in range(len(arr)):
    # window_end = 4
    
    window_sum = arr[window_end] -> 6 += arr[]

  
'''
