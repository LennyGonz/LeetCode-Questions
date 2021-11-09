def last_one_standing(n):
  if n == 1:
    return 1
  if n % 2 == 0:
    return 2 * last_one_standing(n / 2) - 1
  else:
    return 2 * last_one_standing(n / 2) + 1
