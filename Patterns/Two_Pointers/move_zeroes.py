# LeetCode Problem 283

def moveZeroes(nums):
  slow = 0
  
  for fast in range(1,len(nums)):
    if nums[fast] != 0 and nums[slow] == 0:
      # why does this work when line 9 is all in 1 line
      nums[slow], nums[fast] = nums[fast], nums[slow]
      # why won't it work when I try to separate the logic
    
    if nums[slow] != 0:
      slow += 1
  
  return nums

print(moveZeroes([0,1,0,3,12]))

'''
Time Complexity: O(n) - The fast pointer does not visit the same spot twice
Space Complexity: O(1) - All operations are made in-place
'''
