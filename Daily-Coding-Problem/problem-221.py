def nth_sevenish_number(n):
  answer = 0
  bit_place = 0

  while n:
    if (n & 1):
      answer += 7 ** bit_place

    n >>= 1
    bit_place += 1

  return answer
