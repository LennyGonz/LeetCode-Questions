def rand5():
  r = rand7()
  if 1 <= r <= 5:
    return r
  return rand5()
