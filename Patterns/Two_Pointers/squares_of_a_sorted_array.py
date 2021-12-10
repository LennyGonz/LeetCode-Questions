# LeetCode 977 - https://leetcode.com/problems/squares-of-a-sorted-array/
from collections import deque

def sortedSquares(nums):
  result = deque()
  
  left = 0
  right = len(nums) - 1
  
  while left <= right:
    start = abs(nums[left])
    end = abs(nums[right])
    
    if start > end:
      result.appendleft(start*start)
      left += 1
    
    else:
      result.appendleft(end * end)
      right -= 1

  return list(result)

def main():
  nums = [-4,-1,0,3,10]
  print(sortedSquares(nums))

main()

'''
Time: O(N) - N number of elements & and we traverse each element
Space: O(N) - We used a deque that holds all N elements of the input array
'''
