def encode(n):
  s = ""
  while n > 0:
    n, remainder = divmod(n - 1, 26)
    s = chr(65 + remainder) + s
  return s
