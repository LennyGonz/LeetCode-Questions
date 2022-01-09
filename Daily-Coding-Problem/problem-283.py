def regular_numbers(n):
  solution = [1] * n
  i2, i3, i5 = 0, 0, 0

  for i in range(1, n):
    m = min(2 * solution[i2], 3 * solution[i3], 5 * solution[i5])
    solution[i] = m

    if m % 2 == 0:
      i2 += 1
    if m % 3 == 0:
      i3 += 1
    if m % 5 == 0:
      i5 += 1

  return solution

'''
For each value between one and N, we only need to perform a single min operation and increment up to three counters, so this algorithm will run in O(N) time and space.
'''
