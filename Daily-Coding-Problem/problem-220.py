def max_profit(coins, value):
  n = len(coins)
  profit = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    profit[i][i] = coins[i]

  for i in range(n - 1):
    profit[i][i + 1] = max(profit[i][i], profit[i + 1][i + 1])

  for gap in range(2, n):
    for i in range(n - gap):
      j = i + gap
      left = profit[i][j - 2]
      diagonal = profit[i + 1][j - 1]
      bottom = profit[i + 2][j]
      profit[i][i + gap] = max(coins[i] + min(diagonal, bottom), coins[j] + min(left, diagonal))

  return profit[0][-1]
