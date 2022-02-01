'''
LeetCode #339

The input is a list of nested integers and lists

so what we do is iterate over the input list

if the current element is an integer
  we multiply the integer by its depth and add it to totalSum

if the current element is NOT an integer, it must be a nestedList
  so we run a subproblem on the nestedList

We approach this problem recursively -> if we encounter a nestedList - we simply do a recursive call passing the nestedList and increasing the depth
'''

def depthSum(nestedList):
  def dfs(nestedList, depth):
    totalSum = 0
    
    for item in nestedList:
      if item.isInteger():
        totalSum += item.getInteger() * depth
        
      else:
        totalSum += dfs(item.getList(), depth+1)
    
    return totalSum

  return dfs(nestedList, 1)

'''
Time: O(N) - on each nestedList, it iterates over all the nested elements directly inside that list. As each elementcan only be directly inside ONE list, we know that there must only be one-loop iteration for each nested element. This is a total of N-loop iterations. So combined we perform at most 2*N recursive calls and loop iterations
Space: O(N) - the call stack at worst case will have N recursive calls
'''
