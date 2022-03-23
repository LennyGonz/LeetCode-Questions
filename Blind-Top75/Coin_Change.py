'''
LeetCode #322


'''

def coinChange(coins, amount):
  dp = [amount + 1] * (amount + 1)
  dp[0] = 0
  
  for a in range(1, amount+1):
    for c in coins:
      if (a-c) >= 0:
        dp[a] = min(dp[a], 1 + dp[a-c])
  
  return dp[amount] if dp[amount] != amount+1 else -1

def main():
  ex1 = [1,2,5]
  ex1_amount = 11

  ex2 = [2]
  ex2_amount = 3
  
  print("coins: [1,2,4] & amount: 11 - The minimum number of coins to make the amount is:",coinChange(ex1, ex1_amount))
  print(coinChange(ex2, ex2_amount))

main()

'''
Time complexity : O(a*n). where a is the amount, n is denomination count. In the worst case the recursive tree of the algorithm has height of 'a' and the algorithm solves only 'a' subproblems because it caches precalculated solutions in a table. Each subproblem is computed with n iterations, one by coin denomination. Therefore there it is O(a*n).

Space complexity : O(a), where 'a' is the amount to change - We use extra space for the memoization table..
'''
