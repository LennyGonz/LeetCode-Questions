def multi_tables(n, x):
  count = 0
  for i in range(1, n + 1):
    if x % i == 0 and x / i <= n:
      count += 1
  return count
