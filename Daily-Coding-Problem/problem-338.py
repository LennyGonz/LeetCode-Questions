def next_integer_binary(num):
  if num == 0:
    return 0

  count = 0  # The number of 1-bits to clear
  mask = num & ~(num - 1) # Get the lowest set bit
  while not ((num & mask) > 0 and (num & (mask << 1)) == 0):
    num &= ~mask # Clear the set bit
    count += 1
    mask = num & ~(num - 1) # Get the next lowest set bit

  num &= ~mask      # Set the bit to 0
  num |= mask << 1  # Set the next highest bit to 1

  # Set the appropriate number of bits to 1 starting from LSB
  for i in range(count):
    num |= 1 << i

  return num
