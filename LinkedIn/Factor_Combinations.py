'''
Besides 1 and N -> the smallest factor N can have is 2 and the largest factor N can have is (N/2) excluding N of course
ex) N = 12 -> [1,2,3,4,6,12] -> 6 = 12/2

But instead of using N/2 as our upper bound -> we can make it tighter with a sqrt(N)+1 upperbound

So to reduce work and avoid duplicates we search for factors from 2 to sqrt(N)

When we pick a facotr from this range
We take that factor and call another subproblem using that factor

we'll only call another subproblem using that selected factor, IF it actually is a factor, which we determine with: target % i == 0 - if its divisible!

Each recursive call, we're reducing our curr number and appending our current path with curr, which will be the lastest factor of N
The curr argument is used to avoid creating duplicates

ie) if we do 12/3 (curr) there's no point in checking if 12//3 = 4
4 is divisible by anything less than 3 b/c the result factor would be : [3,2,2]
which would have been computed when curr was 2 earlier (in the form of [2,2,3], which is the same as [3,2,2])
'''

import math

def getFactors(num):
  if num == 1:
    return []
  
  res = []
  
  def dfs(path=[], curr=2, target=n):
    if path:
      res.append(path+[target])
      
    for i in range(curr, math.sqrt(target)+1):
      if (target % i == 0):
        dfs(path+[i], i, target//i)
  
  dfs()
  
  return res

'''
Time: O(sqrt(N)) - we iterate over a range of 2 to sqrt(N) numbers
Space: O(H) - height of the call stack
'''  
