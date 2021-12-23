def zigzag(sentence, k):
  n = len(sentence)
  line_matrix = [[' ' for _ in range(n)] for _ in range(k)]

  row = 0
  for col, letter in enumerate(sentence):
    line_matrix[row][col] = letter

    if row == 0:
      descending = True
    elif row == k - 1:
      descending = False

    if descending:
      row += 1
    else:
      row -= 1

  for line in line_matrix:
    print("".join(line))

# This algorithm is O(k * N) in both time and space.
