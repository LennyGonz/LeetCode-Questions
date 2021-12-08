def permute(nums):
  # need to keep track of distinct permutations
  visited = set()
  # a result to return
  result = []
  backtracking(result, visited, [], nums)
  #print("result=", result)
  return result
def backtracking(result, visited, subset, nums):
  print("----")
  print("result", result)
  print("visited", visited)
  print("subset", subset)
  print("----")
  if len(subset) == len(nums):
    result.append(subset)
  for i in range(len(nums)):
    print("i in for loop", i)
    if i not in visited:
      visited.add(i)
      backtracking(result,visited,subset+[nums[i]],nums)
      visited.remove(i)

input = [1, 2, 3]
print(permute(input))
