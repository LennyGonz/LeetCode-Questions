def apply_ops(a, b):
  return [a + b, a - b, a * b, a / b]

def play(nums):
  if len(nums) == 1:
    return nums[0] == 24
  elif len(nums) == 2:
    return any(play([x]) for x in apply_ops(*nums))
  else:
    for i in range(len(nums) - 2):
      for x in apply_ops(*nums[i : i + 2]):
        if play(nums[:i] + [x] + nums[i + 2:]):
          return True
    return False

'''
It is more straightforward to describe the complexity for an arbitrary input of length N.

Initially, we can choose between N - 1 pairs to which we can apply each operation.

Once this is accomplished, we again must choose a pair from the N - 2 remaining.

Continuing this process, we find that in the worst case we will need to apply each operation N! times, leading to a time complexity of O(N!).
'''
