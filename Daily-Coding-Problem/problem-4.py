'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
def firstMissingPositive(nums):
  for index in range(len(nums)):
    if nums[index] <= 0 or nums[index] > len(nums):
      nums[index] = len(nums) + 1

  for num in nums:
    num = abs(num)
    if num <= len(nums) and nums[num-1] >= 0:
      nums[num - 1] *= -1
  
  for index in range(len(nums)):
    if nums[index] > 0:
      return index + 1
  
  return len(nums) + 1

ex1 = [1]
print(firstMissingPositive(ex1))
