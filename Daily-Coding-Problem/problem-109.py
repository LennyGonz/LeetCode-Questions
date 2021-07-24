def swap_bits(x):
  EVEN = 0b10101010
  ODD = 0b01010101
  return (x & EVEN) >> 1 | (x & ODD) << 1

def swap_bits(x):
  return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1
