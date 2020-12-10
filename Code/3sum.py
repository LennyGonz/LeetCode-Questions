'''
Run Time: O(n*n)
Space: O(n)
'''
def threeSum(nums):
  result = []
  nums.sort()
  length = len(nums)
    
  # we need at least 3 elements to continue (index, left, right)
  for index in range(length - 2):
      
    # if nums[i] == nums[i-1] we did the calculations already - skip the redundancy 
    if index > 0 and nums[index] == nums[index-1]:
      continue
    
    left = index + 1
    right = length - 1
    
    # once our pointers cross we've calculated all possible combinations
    while left < right:
      total_sum = nums[index] + nums[left] + nums[right]
      
      # if our total sum is below 0 increase our left pointer
      if total_sum < 0:
          left = left + 1
      
      # if our total sum is greater than 0 decrease our right pointer
      elif total_sum > 0:
          right = right - 1
        
      else:
          # if total_sum = 0 add it to our result list
          result.append([nums[index],nums[left],nums[right]])
          
          # we need to have unique triplets so if the current nums[element] is the same as the next one of course
          # nums[i] + nums[left] + nums[right] = 0 bc it'll be the same triplet so we must increase left twice before restarting the loop
          while left < right and nums[left] == nums[left+1]:
              left = left + 1
          
          # same logic as above, if nums[right] == nums[right-1] then of course nums[i] + nums[left] + nums[right] = 0
          # so to avoid getting the same triplet we must reduce right twice
          while left < right and nums[right] == nums[right-1]:
              right = right - 1
          
          # if nums[left] == nums[left+1] or nums[right] == nums[right-1] here is where we increase/decrease the pointer for the 2nd time
          # otherwise we proceed as we normally would
          left = left + 1
          right = right - 1

  return result


input1 = [-1, 0, 1, 2, -1, -4] #[[-1,-1,2],[-1,0,1]]
input2 = [-2,0,0,2,2] #[[-2,0,2],[-2,0,2]] -- this uses the while statements inside the else statement
print(threeSum(input2))
