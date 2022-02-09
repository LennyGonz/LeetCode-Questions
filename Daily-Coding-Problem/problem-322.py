def make_path(nums, is_negative):
  path = [nums[0]]

  for i in nums[1:]:
    path.append(path[-1] + i)

  if is_negative:
    return [-1 * i for i in path]
  else:
    return path

def jump_path(n):
  is_negative = False

  if n < 0:
    n = -n
    is_negative = True

  k = total = 0
  while total < n or (total > n and (total - n) % 2 != 0):
    k += 1
    total += k

  if total == n:
    return make_path(range(k + 1), is_negative)

  nums = list(range(k + 1))
  index = (total - n) // 2

  return make_path(nums[:index] + [-index] + nums[index + 1:], is_negative)

'''
The sum of 1 + 2 + ... + k evaluates to k * (k + 1) // 2, so the length of our path will be roughly the square root of N.
We must run our while loop for this many iterations, and store a solution path of this length, so the time and space complexity will be O(√N).
'''
