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
  
  return max(count, max_count)


ex1 = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(ex1))
