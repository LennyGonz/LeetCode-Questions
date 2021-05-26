def subsertXORSum(nums):
  ans = 0

  def bt(nums, index, running_xor):
    if index >= len(nums):
      ans += running_xor
    
    else:
      bt(nums, index + 1, nums[index] ^ running_xor)
      bt(nums, index + 1, running_xor)
  
  bt(num, 0, 0)

  return ans
