'''
LeetCode #1004. Max Consecutive Ones III

Similar to Longest Substring with same Letters after Replacement. 

The only difference is that, in the problem, we only have two characters (1s and 0s) in the input arrays.

1. We'll iterate through the array to add one number at a time in the window.
2. We'll also keep track of the maximum number of repeating 1s in the current window (let's call it maxOnesCount). 
    - So at any time, we know that we can have a window with 1s repeating maxOnesCount time, so we should try to replace the remaining 0s.
    - If we have more than 'k' remaining 0s, we should shrink the window as we are not allowed to replace more than 'k' 0s.
'''

def length_of_longest_substring(arr, k):
  # start pointer
  windowStart = 0
  
  # this will hold the length of the longest contiguous subarray having all 1s
  maxLength = 0
  
  # we'll use this to count the number of Ones
  maxOnesCount = 0

  # we'll iterate through the inputArray
  for windowEnd in range(len(arr)):
    
    # if the current element we're on is a 1
    if arr[windowEnd] == 1:
      # increment maxOnesCount
      maxOnesCount += 1
    
    # if we get the point where there are more 0s than 1s 
    # AND
    # we arent allowed to do more than k replacements, we need to shrink our window
    #
    # Current window size is from window_start to window_end, overall we have a maximum of 1s repeating 'max_ones_count' times,
    # this means we can have a window with 'max_ones_count' 1s and the remaining are 0s which should replace with 1s.
    # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we are not allowed to replace more than 'k' 0s
    if (windowEnd-windowStart+1 - maxOnesCount) > k:
      if arr[windowStart] == 1:
        maxOnesCount -= 1
      windowStart += 1
    
    maxLength = max(maxLength, windowEnd-windowStart+1)
  
  return maxLength

'''
Time: O(N), where 'N' is the count of numbers in the input array. We also traverse the input array in 1 pass

Space: O(1), algorithm runs in constant space
'''
