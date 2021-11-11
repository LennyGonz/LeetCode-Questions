def length_of_longest_substring(arr, k):
  windowStart = 0
  maxLength = 0
  maxOnesCount = 0

  for windowEnd in range(len(arr)):
    if arr[windowEnd] == 1:
      maxOnesCount += 1
    
    if (windowEnd-windowStart+1 - maxOnesCount) > k:
      if arr[windowStart] == 1:
        maxOnesCount -= 1
      windowStart += 1
    
    maxLength = max(maxLength, windowEnd-windowStart+1)
  
  return maxLength
