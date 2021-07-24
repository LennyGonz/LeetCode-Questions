def is_shifted(a, b):
  if len(a) != len(b):
    return False

  for i in range(len(a)):
    if all(a[(i + j) % len(a)] == b[j] for j in range(len(a))):
      return True

  return False
