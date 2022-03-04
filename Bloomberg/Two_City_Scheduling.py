'''
A company is planning to interview 2n people.

Given the array costs where costs[i] = [aCosti, bCosti], 
  the cost of flying the ith person to city a is aCosti,
  and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
---------------------------------------------------------------------------------------------------------------

We have 2n people -> n people HAVE to go to city A & n people HAVE to go to city B

So if these are the prices -> [[10,20],[30,200],[400,50],[30,20]]
We need to find a way to send N people to city A as least costly as possible
WHILE
also sending N people to city B as least costly as possible

Strategy:

The problem is to send n persons to city A 
and n persons to city B with minimum cost.

My idea is to send each person to city A -> costs = [[10,20],[30,200],[400,50],[30,20]]

So, totalCost = 10 + 30 + 400 + 30 = 470

Now, we need to send n persons to city B.
Which persons do we need to send city B?

Here, we need to minimize the cost. We have already paid money to go to city A.

So essentially we've sent everyone to cityA and now we'll calculate how much money we get back per candidate
  had we sent them to city B
    - if the valye is positive, it means sending that candidate to city B is more expensive
    - if the value is negative, it means sending that candidate to city B is cheaper

So, we send the candidate to city B -> if it saves the company money

We calculate refund by:
refund[i] = cost[i][1] - cost[i][0]

So, refunds of each person
            20-10, 200-30, 50-400, 20-30
    refund = [10, 170, -350, -10]

Here, refund +ve means we need to pay
             -ve means we will get refund.

So, sort the refund array.
refund = [-350, -10, 10, 170]

Now, get refund for N persons,
totalCost += 470 + -350 + -10 = 110

So, minimum cost is 110

'''

def twoCitySchedCost(costs):
  # Here we'll store the values of the refund
  refund = []

  # we'll calculate the costs of sending every candidate to cityA
  minCost = 0
  
  # we iterate through the input list
  for A, B in costs:
    # calculating the refund of sending each candidate to cityB rather than cityA
    refund.append(B - A)
    
    # while also calculating the cost of sending each candidate to cityA
    minCost += A
  
  # we sort the refund list, from ascending order
  refund.sort()
  
  # we're sending N people to city A
  # and N people to city B
  # so with refund sorted, the best prices will be at the front
  # and the first N candidates will go to city B
  # the other half will go to city A
  for i in range(len(costs)//2):
    minCost += refund[i]
  return minCost

'''
Time: O(NlogN) - due to the sorting - otherwise we do this in one pass of the input array
Space: O(N) - holds the refund value for all the inputs
'''

'''
We can also do this in constant space
'''
def twoCitySchedCost2(costs):
  # Sort by a gain which company has 
  # by sending a person to city A and not to city B
  costs.sort(key = lambda x : x[0] - x[1])
  
  total = 0
  n = len(costs) // 2
  # To optimize the company expenses,
  # send the first n persons to the city A
  # and the others to the city B
  for i in range(n):
    total += costs[i][0] + costs[i + n][1]
  return total
'''
Time: O(NlogN) - due to the sorting - otherwise we do this in one pass of the input array
Space: O(1) - algorithm runs in constant time
'''
def main():
  print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])) #1859
  print(twoCitySchedCost2([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

main()
