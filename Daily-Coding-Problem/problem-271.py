def get_fib_sequence(n):
  a, b = 0, 1
  sequence = [a]

  while a < n:
    a, b = b, a + b
    sequence.append(a)

  return sequence

def fibonacci(array, x):
  n = len(array)
  fibs = get_fib_sequence(n)

  offset = 0
  p, q = len(fibs) - 2, len(fibs) - 1

  while q > 0:
    index = min(offset + fibs[p], n - 1)
    if x == array[index]:
      return True
    elif x < array[index]:
      p -= 2; q -= 2
    else:
      p -= 1; q -= 1
      offset = index

  return False
