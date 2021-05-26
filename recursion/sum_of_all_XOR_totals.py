def subsetXORSum(nums):
  ans = 0
  def bt(nums, index, running_xor):
    nonlocal ans
    if index >= len(nums):
      ans += running_xor
    
    else:
      bt(nums, index + 1, nums[index] ^ running_xor)
      bt(nums, index + 1, running_xor)
  
  bt(nums, 0, 0)

  return ans

example1 = [1,3]
print(subsetXORSum(example1))

'''
There are 2^n subsets, where n is the number of elements in the input array

- []    the empty subset has an XOR total of 0
- [1]   has an XOR total of 1
- [3]   has an XOR total of 3
- [1,3] has an XOR total of 3

0 + 1 + 3 + 2 = 6

3 = 011
1 = 001

XOR compares each bit, if both bits are the same return 0 else return 1
'''
