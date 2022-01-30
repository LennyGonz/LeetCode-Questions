def is_toeplitz(matrix):
  values = {}

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      if i - j not in values:
        values[i - j] = col
      elif values[i - j] != col:
        return False

  return True

'''
Both of these solutions will take O(M * N) time, for a matrix with M rows and N columns, since we must check every cell in the worst case.
'''
