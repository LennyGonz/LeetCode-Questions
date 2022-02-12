def num_pairs(m, n):
  pairs = []

  for i in range(m // 2):
    if i ^ (m - i) == n:
      pairs.append((i, m - i))

  return pairs

'''

This will run in O(M) time and require space up to the number of valid pairs.

However, the use of XOR is a hint that there is a more efficient bitwise solution.

'''
