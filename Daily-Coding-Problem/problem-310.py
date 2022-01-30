def count_set_bits(num):
  count = 0

  while num > 0:
    if num & 1 == 1:
      count += 1
    num >>= 1

  return count

'''
def count_set_bits(num):
  return bin(num).count('1')
'''

def total_set_bits(n):
  if n == 0:
    return 0
  elif n % 2 == 1:
    return (n + 1) // 2 + 2 * total_set_bits(n // 2)
  else:
    return count_set_bits(n) + total_set_bits(n - 1)

'''
In the worst case, each time we divide by two, we may end up with an odd number, so we will have to perform count_set_bits again.
Since each of these operation is O(log N), we arrive at an overall time complexity of O((log N)2).
'''
