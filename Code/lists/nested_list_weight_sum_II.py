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

# Premium LeetCode Question #364
'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

ex1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2 - 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

ex2:
Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1 - 1*3 + 4*2 + 6*1 = 17

Single Pass Solution using a BFS like approach

- Add all the integers at depth 1 - if the current element is NOT an integer push the element into the list for next iterations (the nested list needs to be flattened) or we'll be stuck in an infinite loop

- Now we only initialize depthSum once (at the beginning), And successive depth's intergers are added to it. Once we're done at the current depth, we add it to totalSum. This naturally implements the multiplication logic - lower depth sums are added multiple times to totalSum
'''

def depthSumInverse(nestedList):
  totalSum = 0
  depthSum = 0
  
  while nestedList:
    nextList = []
    
    for item in nestedList:
      if item.isInteger():
        depthSum += item.getInteger()
      
      else:
        for num in item.getList():
          nextList.append(num)
    
    totalSum += depthSum
    nestedList = nextList
  
  return totalSum
