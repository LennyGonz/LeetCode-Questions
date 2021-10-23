def permute(array, permutation):
  for i in range(len(array)):
    element, p = array[i], permutation[i]

    while p != i:
      array[p], element = element, array[p]
      permutation[p], p = p, permutation[p]

    array[i], permutation[i] = element, p
  return array
