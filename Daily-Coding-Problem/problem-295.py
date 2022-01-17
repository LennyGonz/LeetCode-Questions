def pascal(k):
  rows = [0 for _ in range(k + 1)]

  rows[1] = 1
  for i in range(1, k + 1):
    for j in range(i, 0, -1):
      rows[j] += rows[j - 1]

  return rows[1:]

'''
Finally, the mathematicians among you may know that the n + 1th row in Pascal's triangle can be given by the values:

nC0, nC1, ..., nCn, where nCr represents the number of ways of choosing r items out of n.

Therefore, we can implement nCr and use it to elegantly solve our problem.

While this solution also uses O(k) space, the factorial function will bring our run time up to O(k2).
'''

from math import factorial

def nCr(n, r):
  return factorial(n) // factorial(r) // factorial(n - r)

def pascal(k):
  return [nCr(k - 1, i) for i in range(k)]
