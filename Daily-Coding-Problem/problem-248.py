'''
bitwise operations

Consider the following expression: a - k * (a - b). If k = 0, this returns a, whereas if k = 1, this returns b.
So if we had some way to assign k to one of these values based on which term was greater, we would have a solution.
Fortunately, we can do this by shifting (a - b) all the way to the right and taking the most significant bit.

Any positive difference will be shifted down to zero.
Meanwhile, a negative difference will result in 1, because negative numbers are typically stored using two's complement representation.
'''

def max(a, b):
  k = (a - b) >> 31 & 1
  return a - k * (a - b)
