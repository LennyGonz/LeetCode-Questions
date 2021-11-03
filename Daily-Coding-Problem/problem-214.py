def find_length(n):
  max_length = 0

  while n:
    max_length += 1
    n = n & (n << 1)

  return max_length
