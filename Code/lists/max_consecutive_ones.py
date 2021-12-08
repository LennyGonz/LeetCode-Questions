def findMaxConsecutiveOnes(nums):
  max_count, count = 0, 0

  for num in nums:
    if num == 1:
      count += 1
    else:
      # if we're in the else statement we encountered an element that is not a 1
      max_count = max(count, max_count)

      # reset the count variable to start recording the upcoming consecutive ones 
      count = 0
  
  # if we iterate through another subarray and don't encounter 0s, we will not update max_count
  # so we NEED to return max_count and count
  # bc count could be bigger, take for example [1,1,0,1,1,1]
  # after we encounter with the 0, we never enter the else statement again and we're done looping within nums
  # but we never updated max_count = 2 and count = 3
  # so as a percaution we return the max of the 2, so we're absolutely sure we return the max cosecutive ones
  return max(count, max_count)


ex1 = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(ex1))
