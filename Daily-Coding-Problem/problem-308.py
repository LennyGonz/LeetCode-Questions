def split(expression):
  operands, operators = [], []

  for value in expression:
    if value in {'T', 'F'}:
      operands.append(value)
    else:
      operators.append(value)

  return operands, operators

def solve(expression):
  operands, operators = split(expression)

  n = len(operands)
  T = [[0 for _ in range(n)] for _ in range(n)]
  F = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    if operands[i] == 'T':
      T[i][i] = 1; F[i][i] = 0
    else:
      T[i][i] = 0; F[i][i] = 1

  for gap in range(1, n):
    for i in range(n - gap):
      j = i + gap

      for k in range(i, j):
        all_options = (T[i][k] + F[i][k]) * (T[k+1][j] + F[k+1][j])

        if operators[k] == '&':
          T[i][j] += T[i][k] * T[k+1][j]
          F[i][j] += (all_options - T[i][j])

        elif operators[k] == '|':
          F[i][j] += F[i][k] * F[k+1][j]
          T[i][j] += (all_options - F[i][j])

        elif operators[k] == '^':
          T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
          F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]

  return T[0][n - 1]

'''
The space complexity will be O(N2), where N is the number of operands, in order to store the T and F matrices. 
Calculating each cell in both matrices requires us to calculate the result for each split point, which is O(N), so the overall algorithm will take O(N3) time.
'''
