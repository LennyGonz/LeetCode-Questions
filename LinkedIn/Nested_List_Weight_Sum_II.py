'''
LeetCode #364

weight = maxDepth - (depth of the integer) + 1

If we have: [[2,3],4,[1,[3,2,[5]]],1] - maxDepth here would be 4

elements: 4 and 1 have a depth of 1 - weight of these elements would be 4
elements: 2,3 and 1 have a depth of 2 - weight of these elements would be 3
elements: 3 and 2 have a depth of 3 - weight of these elements would be 2
element: 5 has a depth of 4 - weight of these elements would be 1

1 + 4
2 + 3 + 1 + 1 + 4
3 + 2 + 2 + 3 + 1 + 1 + 4
5 + 3 + 2 + 2 + 3 + 1 + 1 + 4

* notice we had (1+4) 4 times === (4*4) + (1*4)
* notice we had (2+3+1) 3 times === (2*3) + (3*3) + (1*3)
* notice we had (3+2) 2 times === (3*2) + (3*2)
* notice we had (5) 1 times === (5*1)

We don't calculate weight, we simply to repeated addition for each layer we unfold in the input array
'''

def depthSumInverse(nestedList):
  totalSum = 0
  levelSum = 0
  
  while nestedList:
    next_level_list = []
    
    for item in nestedList:
      if item.isInteger():
        levelSum += item.getInteger()
      else:
        for num in item.getList():
          next_level_list.append(num)
    
    # this is where we do the repeated addition
    totalSum += levelSum
    nestedList = next_level_list
  
  return totalSum

'''
Time: O(N)
Space: O(N) - worst case for space complexity occurs where the majority of elements are at the same depth, as all the elements at that depth will be in the array at the same time, therefore worst case O(N)
'''
