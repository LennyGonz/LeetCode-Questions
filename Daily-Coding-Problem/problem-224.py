def smallest_impossible_sum(nums):
  impossible_sum = 1
  for n in nums:
    if n <= impossible_sum:
      impossible_sum += n
    else:
      break
  return impossible_sum
