NUM_BITS = 32
NUM_BITS_IN_CACHE = 8

def reverse_naive(n, num_bits):
  reversed_num = 0
  for i in range(num_bits):
    j = n >> i & 1
    reversed_num += j << (num_bits - i - 1)
  return reversed_num

def preprocess():
  cache = {}
  for i in range(2 ** NUM_BITS_IN_CACHE):
    cache[i] = reverse_naive(i, NUM_BITS_IN_CACHE)
  return cache

preprocessed = preprocess()

def reverse_bits(n):
  result = 0
  mask = 2 ** NUM_BITS_IN_CACHE - 1
  for i in range(NUM_BITS // NUM_BITS_IN_CACHE):
    relevant = n >> (i * NUM_BITS_IN_CACHE) & mask
    result += preprocessed[relevant] << NUM_BITS - ((i + 1) * NUM_BITS_IN_CACHE)
  return result
