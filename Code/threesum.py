def threeSum(nums):
  res = []
  nums.sort()

  length = len(nums)

  for index in range(length - 2):
    print('++++')
    print("nums[index]", nums[index])
    print('++++')
    if index > 0 and nums[index] == nums[index - 1]:
      print('Inside the initial if','nums[index]',nums[index], '||','nums[index-1]',nums[index-1])
      continue

    left = index + 1
    right = length - 1

    while left < right:
      total = nums[index] + nums[left] + nums[right]

      if total < 0:
        left = left + 1
      
      elif total > 0:
        right = right - 1

      else:
        res.append([nums[index],nums[left],nums[right]])

        # suppose you are getting duplicate triplets
        while left < right and nums[left] == nums[left+1]:
          left = left + 1
        
        while left < right and nums[right] == nums[right-1]:
          right = right - 1
        
        left = left + 1
        right = right - 1

  return res

input1 = [-1,0,1,2,-1,-4]
print(threeSum(input1))
