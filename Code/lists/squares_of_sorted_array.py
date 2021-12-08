from collections import deque 

def squares(nums):
  answer = deque()
  left = 0
  right = len(nums) - 1

  while left <= right:
    start = abs(nums[left])
    end = abs(nums[right])

    if start > end:
      answer.appendleft(start * start)
      left += 1
    else:
      answer.appendleft(end * end)
      right -= 1
    
  return list(answer)

ex1 = [-4,-1,0,3,10]

print(squares(ex1))
