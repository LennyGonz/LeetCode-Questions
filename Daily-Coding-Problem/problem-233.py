def fib(n: int):
  if n <= 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

cache = {0: 0, 1: 1}

def fib(n: int):
  if n in cache:
    return cache[n]
  else:
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

def fib(n: int):
  if n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(n - 1):
      a, b = b, a + b
    return b
