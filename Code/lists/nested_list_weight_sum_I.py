# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Premium LeetCode #339
'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

ex1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1 - 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

ex2:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
'''

################
# DFS Approach #
################
def depthSum2(nestedList):
  def dfs(nestedList, depth):
    totalSum = 0
    for item in nestedList:
      # if item is an integer
      if item.isInteger():
        # then we multiply the integer by its depth then add it to totalSum
        totalSum += item.getInteger() * depth
      
      # if item is a nestedList
      else:
        # we keep peeling the layers and increase depth accordingly by 1
        totalSum += dfs(item.getList(), depth + 1)
    return totalSum

  return dfs(nestedList, 1)

################
# BFS Approach #
from collections import deque
################
def depthSum(nestedList):
  queue = deque(nestedList)

  depth = 1
  total = 0

  while len(queue) > 0:
    for _ in range(len(queue)):
      nested = queue.pop()
      if nested.isInteger():
        total += nested.getInteger() * depth
      else:
        queue.extendedleft(nested.getList())
    depth += 1

  return total

print(depthSum2([1, [4, [6]]]))