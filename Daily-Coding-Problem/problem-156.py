def num_squares(n):
  if n == 0:
    return 0

  cache = [inf for i in range(n + 1)]
  cache[0] = 0
  for i in range(1, n + 1):
    j = 1
    while j * j <= i:
      cache[i] = min(cache[i], cache[i - j*j] + 1)
      j += 1

  return cache[n]
