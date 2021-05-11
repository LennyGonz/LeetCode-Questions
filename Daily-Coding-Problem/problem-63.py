def check_word_right(matrix, r, c, word):
  word_len = len(word)
  row_len = len(matrix[0])
  if word_len != row_len - c:
    return False
  for c1, c2 in zip(word, (matrix[r][i] for i in range(c, row_len))):
    if c1 != c2:
      return False
  return True

def check_word_down(matrix, r, c, word):
  word_len = len(word)
  col_len = len(matrix)
  if word_len != col_len - r:
    return False
  for c1, c2 in zip(word, (matrix[i][c] for i in range(r, col_len))):
    if c1 != c2:
      return False
  return True

  return ''.join([matrix[i][c] for i in range(r, min(col_len, length))])

def word_search(matrix, word):
  for r, row in enumerate(matrix):
    for c, val in enumerate(row):
      if check_word_right(matrix, r, c, word):
        return True
      if check_word_down(matrix, r, c, word):
        return True
  return False
