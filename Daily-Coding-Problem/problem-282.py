def triplet(array):
  array = sorted([x ** 2 for x in array])

  for c in range(len(array) - 1, 1, -1):
    a, b = 0, c - 1

    while a < b:
      if array[a] + array[b] == array[c]:
        return True
      elif array[a] + array[b] < array[c]:
        a += 1
      else:
        b -= 1

  return False

# With this algorithm, we only need to iterate through the array once for each value of c, so the runtime will be O(N^2).
