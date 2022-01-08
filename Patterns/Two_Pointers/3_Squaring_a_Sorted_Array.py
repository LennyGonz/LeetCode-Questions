from collections import deque

def make_squares(arr):
  squares = deque()
  
  left = 0
  right = len(arr) - 1
  
  while left <= right:
    start = abs(arr[left])
    end = abs(arr[right])
    
    if start > end:
      squares.appendleft(start * start)
      left += 1
    
    else:
      squares.appendleft(end * end)
      right -= 1
  
  return list(squares)

def main():
  print(make_squares([-2,-1,0,2,3])) # [0,1,4,4,9]
  print(make_squares([-3,-1,0,1,2])) # [0,1,1,4,9]
  
main()
