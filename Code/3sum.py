def threeSum(nums):
  nums.sort()
  result = []
  lenOfNums = len(nums)
  print('lenOfNums',lenOfNums)

  for index in range(lenOfNums):
    print("index:", index)
    ## why does this matter nums[index] == nums[index - 1] ??
    if index > 0 and nums[index] == nums[index - 1]:
      print("nums[index]:", nums[index], "||", 'nums[index-1]', nums[index-1]);
      continue
    
    head = index + 1
    print("head = index + 1 -->", head)
    
    end = lenOfNums - 1
    print("end = lenOfNums -  1 -->", end)

    print('++++++++++++')

    # this condition for a while loop -> makes sure we stop irterating once our pointers cross
    # seems like head = head of the array & end = end of the array and we meet in the middle???
    while head < end:
      if nums[index] + nums[head] + nums[end] == 0:
        print("if nums[index]",nums[index],"nums[head]",nums[head],'nums[end]',nums[end])
        result.append([nums[index], nums[head], nums[end]])
        head += 1
        print("head:", head)

        while head < end and nums[head] == nums[head - 1]:
          head += 1
          print("head inside the while", head)
        end -= 1
        print("end", end)

        while head < end and nums[end] == nums[end+1]:
          end -= 1
        
        print("------------")
      
      elif nums[index] + nums[head] + nums[end] < 0:
        print("elif nums[index]",nums[index],"+nums[head]",nums[head],'nums[end]',nums[end], "< 0")
        head += 1
        while head < end and nums[head] == nums[head - 1]:
          print("elif - while head",head, "<","end", end, 'and nums[head]', nums[head], "== nums[end]", nums[end])
          head += 1
          print('updated head:',head)
        print("------------")
      else:
        print("else")
        end -= 1
        print("end")
        while head < end and nums[end] == nums[end + 1]:
          print("else - while head",head, "< end", end, "and nums[end]", nums[end], '== nums[end+1]', nums[end+1])
          end -= 1
          print("updated end", end)

  return result

input1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(input1))
