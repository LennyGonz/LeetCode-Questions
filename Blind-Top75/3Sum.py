'''
LeetCode #15 - 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 

such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

----------------------------------------------------------------------------------

'''

def threeSum(nums):
  # result list that will hold all our triplets - so res will be a list of lists
  res = []
  
  # then we sort the input array - to make it easier to easier to avoid/detect duplicates
  nums.sort()
  
  # we use the outer loop to find the first value in the triplet
  # we want to use each number in the input array as a possible first value
  for index, val in enumerate(nums):
    # we begin checking for duplicates on the 2nd element of the input array
    # if the 2nd element is the same as the first element - skip this iteration
    if index > 0 and val == nums[index - 1]:
      # we don't want to resue the same value so we skip this entire iteration
      continue
    
    # we use the 2 pointer solution for the remainder portion of the array, to basically solve the TwoSum problem
    left, right = index + 1, len(nums) - 1
    
    # we use this inner loop to basically solve Two_Sum - and find the other 2 values in the triplet
    # left and right CANT be equal
    while left < right:
      # compute the sum
      threeSum = val + nums[left] + nums[right] 
      
      # if the sum is greater than 0
      if threeSum > 0:
        # we need to decrease it - so we move our right pointer down
        right -= 1
      
      # if the sum is too small
      elif threeSum < 0:
        # so we shift our left pointer up
        left += 1
      
      # if threeSum is equal to 0
      else:
        # we add it to our result list
        res.append([val, nums[left], nums[right]])

        # and we need to update our pointers
        # however we only need to update 1 pointer because our if or elif will update the other
        left += 1
        
        # our pointers cant have duplicates either - so we need to make sure left isnt pointing to the same number as before
        while nums[left] == nums[left-1] and left < right:
          left += 1

  return res

def main():
  nums = [-1,0,1,2,-1,-4]
  print(threeSum(nums)) # [[-1,-1,2],[-1,0,1]]
main()

'''
Time: O(N^2) - We use a nested loop to find the triplets & N^2 is greater than O(nlogn) which is the time it takes for sorting
Space: O(1) - our algorithm runs in constant space
'''
