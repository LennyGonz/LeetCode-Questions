def power_of_four(num):
  if num & (num - 1):
    return False

  count = 0
  while num > 1:
    num >>= 1 
    count += 1

  if count % 2 == 0:
    return True
  else:
    return False

'''
Unfortunately this solution may still run in logarithmic time, as there may be O(log N) zeros in the binary representation of our integer.
'''

def power_of_four(num):
  return num & (num - 1) == 0 and num % 3 == 1
