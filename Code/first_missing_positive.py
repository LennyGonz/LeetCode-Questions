def firstMissingPositive(nums):
  # cleaning up
  for index in range(len(nums)):
    print("index", index)
    if nums[index] <= 0 or nums[index] > len(nums):
      print("Cleaning Up - Before",nums[index])
      nums[index] = len(nums) + 1
      print("Cleaning Up - After",nums[index])
      print("******")
  
  #placing our marker
  for num in nums:
    print("num", num)
    num = abs(num)
    print("abs(num)",abs(num))
    if num <= len(nums) and nums[num - 1] >= 0:
      nums[num - 1] *= 1
      print("nums[num - 1]", nums[num - 1])
  
  #final step for getting the answer
  for index in range(len(nums)):
    print("final step - index", index)
    if nums[index] > 0:
      print("nums[index]",nums[index])
      return index + 1
  
  return len(nums) + 1

input1 = [7, 8, 9, 11, 12]
print(firstMissingPositive(input1))
