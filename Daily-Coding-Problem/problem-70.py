def sum_of_digits(n):
  current_sum = 0
  while n > 0:
    current_sum += n % 10
    n = n // 10
  return current_sum

def perfect(n):
  i, current = 0, 0
  while current < n:
    i += 1
    if sum_of_digits(i) == 10:
      current += 1
  return i
