def duplicate(lst):
  n = len(lst) - 1
  return sum(lst) - (n * (n + 1) // 2)
