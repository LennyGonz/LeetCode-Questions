import heapq

def primes():
  composite = []
  i = 2

  while True:
    if composite and i == composite[0][0]:
      while composite[0][0] == i:
        multiple, p = heapq.heappop(composite)
        heapq.heappush(composite, [multiple + p, p])

    else:
      heapq.heappush(composite, [i*i, i])
      yield i

    i += 1
