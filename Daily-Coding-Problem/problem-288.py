def get_digits(num):
  digits = str(num)
  
  if len(digits) == 4:
    return digits
  else:
    return '0' * (4 - len(digits)) + digits

def kaprekar_steps(num, steps=0):
  if num == 6174:
    return steps

  digits = get_digits(num)
  num = int(''.join(sorted(digits, reverse=True))) - int(''.join(sorted(digits)))

  return kaprekar_steps(num, steps + 1)

'''
It can be seen experimentally that all (non-repeating) values of input between 1000 and 9999 terminate in fewer than eight steps. Since the bulk of each step consists of sorting strings of length four and performing subtraction, the time complexity is basically O(1).

The first algorithm takes O(1) space, and the second will require space proportional to the number of steps to maintain the stack of recursion calls. However, since this number cannot exceed seven, as discussed above, this too can be considered constant.
'''
