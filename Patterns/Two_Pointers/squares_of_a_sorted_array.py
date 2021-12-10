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
