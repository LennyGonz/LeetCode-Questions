def threeSum(nums):
  nums.sort()
  result = []
  lenOfNums = len(nums)

  for index in range(lenOfNums):
    print("index:", index)
    ## why does this matter nums[index] == nums[index - 1] ??
    if index > 0 and nums[index] == nums[index - 1]:
      print("nums[index]:", nums[index], "||", 'nums[index-1]', nums[index-1]);
      continue
    
    head = index + 1
    print("head = index + 1 -->", head)
    
    end = lenOfNums - 1
    print("end = lenOfNums-1 -->", end)

    print('++++++++++++')

    while head < end:
      print("if nums[index]",nums[index],"nums[head]",nums[head],'nums[end]',nums[end])
      if nums[index] + nums[head] + nums[end] == 0:
        result.append([nums[index], nums[head], nums[end]])
        head += 1

        while head < end and nums[head] == nums[head-1]:
          head += 1
        end -= 1

        while head < end and nums[end] == nums[end+1]:
          end -= 1
        
        print("------------")
      
      elif nums[index] + nums[head] + nums[end] < 0:
        print("elif nums[index]",nums[index],"+nums[head]",nums[head],'nums[end]',nums[end], "< 0")
        head += 1
        while head < end and nums[head] == nums[head-1]:
          head += 1
        print("------------")
      else:
        print("else")
        end -= 1
        while head < end and nums[end] == nums[end + 1]:
          end -= 1

  return result

input1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(input1))
