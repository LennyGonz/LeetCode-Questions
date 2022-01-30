def and_product(m, n):
  i = 0

  while m != n:
    m >>= 1
    n >>= 1
    i += 1

  return n << i

'''
There will be roughly log N bits in the binary representation of N, so this solution will run in O(log N) time and O(1) space.
'''
