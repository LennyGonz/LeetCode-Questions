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

ex2 = []
print(firstMissingPositive(ex2))

ex3 = [1, 2, 3, 4, 5]
print(firstMissingPositive(ex3))


# #####################################
# This solution runs in O(n) time & space
# #####################################

def firstMissingPositive(nums):
  s = set(nums)
  i = 1

  while i in s:
    i += 1
  
  return i

ex1 = []
print(firstMissingPositive(ex1))

[-1,-2,-3,-4,-5,1,2,3,4,4]

# #################################################
# This solution runs in O(n) time & constant space
# #################################################

def firstMissingPositive(nums):
  if not nums:
    return 1
  
  for index, value in enumerate(nums):
    # while the previous element is not the same as the curent element
    while index + 1 != nums[index] and 0 < nums[index] <= len(nums):
      v = nums[index]
      nums[index], nums[v - 1] = nums[v - 1], nums[i]
      if nums[i] == nums[v - 1]:
        break

  for i, num in enumerate(nums, 1):
    if num != i:
      return i
  
  return len(nums) + 1
