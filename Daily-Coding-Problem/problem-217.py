def next_sparse_number(num):
  # Convert to list of bits, from least to most significant.
  b = []
  while num:
    b.append(num & 1)
    num = num >> 1
  b.append(0)

  # Find the places where 011 exists, and turn them into 100 with trailing zeros.
  highest_zeroed_bit = 0
  for i in range(len(b) - 2):
    if b[i] and b[i + 1] and not b[i + 2]:
      b[i + 2] = 1
      for j in range(i + 1, highest_zeroed_bit - 1, -1):
        b[j] = 0
      highest_zeroed_bit = i + 1

  # Convert back to integer.
  num = 0
  for i in range(len(b)):
    num += b[i] * (1 << i)
  return num
