def num_paths(current, jumps, visited, n):
  if n - 1 == 0:
    return 1

  paths = 0
  for next_number in range(1, 10):
    if next_number not in visited:
      if (current, next_number) not in jumps or jumps[(current, next_number)] in visited:
        visited.add(next_number)
        paths += num_paths(next_number, jumps, visited, n - 1)
        visited.remove(next_number)

  return paths

def unlock_combinations(n):
  jumps = {(1, 3): 2, (1, 7): 4, (1, 9): 5,
           (2, 8): 5,
           (3, 1): 2, (3, 7): 5, (3, 9): 6,
           (4, 6): 5, (6, 4): 5,
           (7, 1): 4, (7, 3): 5, (7, 9): 8,
           (8, 2): 5,
           (9, 1): 5, (9, 3): 6, (9, 7): 8}

  return 4 * num_paths(1, jumps, set([1]), n) + \
          4 * num_paths(2, jumps, set([2]), n) + \
          1 * num_paths(5, jumps, set([5]), n)
