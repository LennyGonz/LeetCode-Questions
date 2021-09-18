def first_recurring(str):
  checker = 0
  for c in str:
    val = ord(c) - ord('a')
    if (checker & (1 << val)) > 0:
      return c
    checker |= (1 << val)
  return None
