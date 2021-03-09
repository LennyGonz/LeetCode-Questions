def firstMissingPositive(nums):
  # cleaning up
  for index in range(len(nums)):
    if nums[index] <= 0 or nums[index] > len(nums):
      nums[index] = len(nums) + 1
  
  #placing our marker
  for num in nums:
    num = abs(num)
    if num <= len(nums) and nums[num - 1] >= 0:
      nums[num - 1] *= 1

  #final step for getting the answer
  for index in range(len(nums)):
    if nums[index] > 0:
      return index + 1
  
  return len(nums) + 1

input1 = [7, 8, 9, 11, 12]
print(firstMissingPositive(input1))

input2 = [1]
print(firstMissingPositive(input2))
