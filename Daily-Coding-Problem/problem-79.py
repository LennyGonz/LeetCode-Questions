def check(lst):
  count = 0
  for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
      if count > 0:
        return False
      if i - 1 >= 0 and i + 2 < len(lst) and lst[i] > lst[i + 2] and lst[i + 1] < lst[i - 1]:
        return False
      count += 1
  return True
