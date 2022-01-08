# Leetcode 15 (3Sum)

def threeSum(nums):
  nums.sort()
  triplets = []
  
  def search_pairs(nums, target_sum, left, triplets):
    right = len(nums) - 1
    
    while left < right:
      # we need to calculate the sum
      current_sum = nums[left] + nums[right]
      
      # if current_sum == target_sum - then we have a valid unique triplet
      # in other words, check to see if the pair we have right now satisfies Y + Z == -X
      if current_sum == target_sum:
        # we have a valid triplet - we need to re-negate target_sum (back to original value), nums[left], nums[right]
        triplets.append([-target_sum, nums[left], nums[right]])
        
        # need to adjust the left and right pointers
        left += 1
        right -= 1
        
        # make sure with the adjustments of the pointers dont cause us to use duplicate elements in the next iteration
        # if they did, adjust the appropriate pointer
        while left < right and nums[left] == nums[left-1]:
          left += 1
        while left < right and nums[right] == nums[right+1]:
          right -= 1
      
      # we need a bigger pair with a bigger sum
      elif target_sum > current_sum:
        left += 1
      
      # we need a pair with a smaller sum
      else:
        right -= 1
  
  for i in range(len(nums)):
    # check that -X (-nums[i]) is not the same element as the element prior (nums[i-1])
    # if we have the same element, we skip the current iteration to avoid duplicate triplets
    if i > 0 and nums[i] == nums[i-1]:
      continue
    
    # if we skipped the if-statement - we're working with unique triplets
    search_pairs(nums, -nums[i], i+1, triplets)
  
  return triplets

def main():
  print(threeSum([-3,0,1,2,-1,1,-2])) # [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
  print(threeSum([-5,2,-1,-2,3])) # [[-5, 2, 3], [-2, -1, 3]]

main()
