def find_denominations(array):
  coins = set()

  for i, val in enumerate(array[1:], 1):
    if val > 0:
      for coin in coins:
        if array[(i - coin)] > 0 and ((i - coin) not in coins or (i - coin) <= coin):
          val -= 1
      if val > 0:
        coins.add(i)

  return coins

'''
The time complexity of this algorithm is O(M * N), where M is the number of coins in our solution and N is the length of our input.
The space complexity will be O(M), since we require extra space to store the set of solution coins.
'''
