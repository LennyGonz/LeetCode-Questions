'''
LeetCode #605

[1,0,1]
1 empty spot won't allow us to plant 1 flower

[1,0,0,1]
2 consecutive empty plots won't allow us to plant 1 flower

[1,0,0,0,1]
3 consecutive empty plots mean we can plant 1 flower

However, if we have: [0,0,1] -> here we can plant a flower
So if we think of the edges as empty spots, we can better determine if we have the space to plant a flower
trick -> 0 [0,0,1] 0 - we can pretend there are 0s on the outside

However, this method requires altering the input array, thus increasing our space complexity (answer on the bottom)

rather than checking if all 3 spots are empty, we keep track of how many contiguous empty spots we saw
Which is why if the first position in the flowerbed is empty (denoted by 0), then empty will be 1
when we start iterating over flowerbed, the first position is empty so, empty +=1 -> we just "saw" 2 empty contiguous plots
SO we follow the same strategy but without altering the input array

we need to do integer division, because if empty is 0 then we'll have (-1/2) and in python that rounds down (-1) not 0 (like in other languages)
So we do int((empty-1)/2), we add the -1 because we need to offset the potential extra 1 we added

From there we just decrement n by the # of plants we could've planted
Once we decrement n -> we need to reset empty back to 0

The else condition just increments empty by 1 - because that means the current plot in the flowerbed is empty

When we finish iterating over the flowerbed, we do 1 last thing

IF the last position in the flowerbed is empty then we potentially have to add the number of flowers we could have planted since the last position we saw flower and reset empty

We don't have the -1 in the last n calculation because we're assuming that there's 1 last empty position at the end of the flowerbed
'''

def canPlaceFlowers(flowerbed, n):
  # if the very first element is a 1 - empty will be 0
  # if the very first element is a 0 - empty will be 1
  empty = 0 if flowerbed[0] else 1
  
  for f in flowerbed:
    if f:
      n -= int((empty-1)/2) #integer division
      empty = 0
    else:
      empty += 1
  
  n -= (empty) // 2
  
  return n <= 0

'''
Time: O(N)
Space: O(1)
'''

def canPlaceFlowers(flowerbed, n):
  f = [0] + flowerbed + [0]
  
  # we want to skip the first and last elements bc we added 0s there
  for i in range(1, len(f)-1):
    if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
      # we need to update the array, so we know not to violate the adjacent plant rule
      f[i] = 1
      # decrement n, by 1 each time we successfully find a place for a plant
      n -= 1
  
  return n <= 0

'''
Time: O(N) - One pass
Space: O(N) - Altered the input array 
'''
