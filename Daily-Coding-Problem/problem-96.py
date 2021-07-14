def permute(nums):
  def helper(nums, index, output):
    if index == len(nums) - 1:
      output.append(nums.copy())
    for i in range(index, len(nums)):
      nums[index], nums[i] = nums[i], nums[index]
      helper(nums, index + 1, output)
      nums[index], nums[i] = nums[i], nums[index]

  output = []
  helper(nums, 0, output)
  return output
