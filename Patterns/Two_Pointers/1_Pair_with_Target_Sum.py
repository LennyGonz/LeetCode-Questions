# LeetCode 1 - Two Sum

def pair_with_targetSum(arr, target_sum):
  start = 0
  end = len(arr) - 1
  
  while (start < end):
    if (arr[start] + arr[end] == target_sum):
      return [start,end]
    
    elif (arr[start] + arr[end] < target_sum):
      start += 1
    
    else:
      end -= 1
  
  return [-1,-1]

def main():
  print(pair_with_targetSum([1,2,3,4,6],6)) # [1,3]
  print(pair_with_targetSum([2,5,9,11],11)) # [0,2]

main()
