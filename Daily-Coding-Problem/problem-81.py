def get_permutations(digits, mapping):
  digit = digits[0]

  if len(digits) == 1:
    return mapping[digit]

  result = []
  for char in mapping[digit]:
    for perm in get_permutations(digits[1:], mapping):
      result.append(char + perm)
  return result
