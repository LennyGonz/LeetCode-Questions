'''
LeetCode #121 - Best Time to Buy and Sell Stock

* Remember the saying about stocks -> Buy low and Sell high

Using this as an example: [7,1,5,3,6,4]

We cant return 6 (7-1) bc you would buy at 7 and sell at 1
So we move left to right, using left as the buy pointer and right as the sell pointer

if the left pointer is greater than our right pointer 
  that's essentially saying we're buying high and selling low
    therefore we don't want that and we move both pointers

if the left pointer is less than our right pointer
  that's essentially saying we're buying low and selling high
    however, when we calculate profit, we only update maxProfit if profit is greater than the current maxProfit

* In the case where left > right -> we move the left pointer to wherever the right pointer is currently located
    because essentially right just found a value less than the one left is currently at
      and we want left to always point to the smallest value in the input array
      and regardless of what happens, we want to move the right pointer up by 1 value every iteration
'''
def maxProfits(prices):
  left = 0
  right = 1
  maxProfit = 0
  
  while right < len(prices):
    # buy low and sell high
    if prices[left] < prices[right]:
      profit = prices[right] - prices[left]
      
      maxProfit = max(maxProfit, profit)
    
    else:
      # if right is currently at a smaller value
      # we move left to that point - so left and right temporarily point to the same value
      left = right
    
    # regardless of the situation
    # we always move right up by 1
    # at the end of every iteration
    right += 1
  
  return maxProfit

print(maxProfits([7,1,3,4,5,6])) #5
print(maxProfits([7,1,5,3,6,4])) #5
