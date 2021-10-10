'''
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].

In the previous 2 examples, we get the size of the subarray and we simply maintain it throughout the algorithm 
But now, we have to shrink the window as much as we can! ~~ this is the twist

However, the strategy remains (more or less) the same

We want to keep track of our window size, window sum, minimum length of the window whose sum >= s

Since we want the window to shrink while the sum of the window remains >= s
We need to use a while-loop, because if we use an if-statement (like in the previous examples) we set the window to whatever size the window is whose size >= s

In the while-loop we iteratively reduce the window_size until it can no longer satisfy the condition, update the min_length of the subarray, and move our window_start to properly calculate the size of the subarray

And finally after all that, if no subarray is found we return 0
'''

def smallest_subarray_with_given_sum(arr, s):
  window_sum = 0
  min_length = float('inf')
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]# add the next element

    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end-window_start+1)
      window_sum -= arr[window_start]
      window_start += 1
  
  if min_length == float('inf'):
    return 0
  
  return min_length

print(smallest_subarray_with_given_sum([2,1,5,2,3,2], 7))
print(smallest_subarray_with_given_sum([2,1,5,2,8], 7))
print(smallest_subarray_with_given_sum([3,4,1,1,6],8))

'''
Time: O(n)
The time complexity of the above algorithm will be O(N)O(N).
The outer for loop runs for all elements, and the inner while loop processes each element only once.
Therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

Space: O(1)
'''
