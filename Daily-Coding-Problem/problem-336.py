from math import log

def get_factorials(n):
  factorials = {0: 1}

  for i in range(1, n + 1):
    factorials[i] = i * factorials[i - 1]

  return factorials

def choose(factorials, n, k):
  return factorials[n] // factorials[n - k] // factorials[k]

def ways(n, f):
  if n <= 2:
    return 1

  height = int(log(n)) + 1
  bottom = n - (2 ** height - 1)

  left = 2 ** (height - 1) - 1 + min(2 ** (height - 1), bottom)
  right = n - left - 1

  return choose(f, n - 1, left) * ways(left, f) * ways(right, f)

def num_heaps(n):
  factorials = get_factorials(n)
  return ways(n, factorials)

'''
To improve our efficiency, we precalculate each factorial up to N beforehand, so that our choose method runs in O(1) time.
This precompuation will require O(N) time and O(N) space.

We will need to call ways a number of times equal to the height of the heap, or log N, and each call takes around log N to run.
As a result, our time complexity can be given as O(N + log2N).
'''
