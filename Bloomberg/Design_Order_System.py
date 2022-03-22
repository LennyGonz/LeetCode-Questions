'''
You have to design an order system that keeps track of the minimum amount of orders per day.
You also have to keep track of the number of orders that day. The last order that is added to the system is executed first

The system is composed of 3 methods:

1) addOrder(integer amount) -> None: adds to the list of orders
2) executeOrder(self) -> integer: executes the last order put in to the system
3) extractMinimumOrder(self) -> integer: returns the smallest order so far

So you arent given the constructor, part of the challenge is to decide on the data structure to control the incoming stream of orders
All methods must run in constant time O(1) and no loops
'''

class OrderSystem:
  def __init__(self) -> None:
    # this will keep track of all incoming orders
    self.orders = []
    # this will keep track of the smallest order so far
    self.mins = []
  
  '''
  initially mins will be empty so we immediately append it
  and regardless the order needs to be inserted into orders

  however after the first exection, we need to check the last order added and the smallest order so far
  - if the last order added is not smaller than the min, we dont add
  - if the last order added IS smaller than the min, we add
  '''
  def addOrder(self, amount: int) -> None:
    # amount = 15
    if not self.mins:
      self.mins.append(amount)
    
    self.orders.append(amount)

    x = self.orders[-1]

    if x <= self.mins[-1]:
      self.mins.append(x)

  '''
  We NEED to execute the last order add -> so immediately we pop off the last element from orders

  HOWEVER if that last order added is ALSO the smallest order so far we must update the min array as well
      so we pop it off
  
  if the last order added was not the smallest so far, doesn't matter
  we keep both lists appropriately updated

  if we don't do this and we have mins[13,9,1], orders[13,9,1] min = 1
  and we executeorder() -> mins[13,9,1], orders[13,9] (notice how mins still has 1 and 1 is no longer in the orders list)
  and say we executeorder() again -> mins[13,9,1], orders[13,9] we have to execute order 9, but order 1 is no longer the min, so our lists are out of sync
  '''
  def executeOrder(self) -> None:
    x = self.orders.pop()

    if x == self.mins[-1]:
      self.mins.pop()

    return x

  '''
  mins if properly maintained, its last element will be the minimum so far
  so we simply return whatever is at the top
  '''
  def extractMinOrder(self) -> None:
    return self.min[-1]

ordersys = OrderSystem()
ordersys.addOrder(13) # mins[13], orders[13]
ordersys.addOrder(9) # mins[13,9], orders[13,9]
ordersys.addOrder(11) # mins[13,9], orders[13,9,11]
ordersys.extractMinOrder() # 9
ordersys.executeOrder() # 11
ordersys.extractMinOrder() # 0
ordersys.addOrder(1) # mins[13,9,1], orders[13,9,1] min = 1
ordersys.executeOrder() #  mins[13,9,1], orders[13,9,1]
ordersys.extractMinOrder() #  mins[13,9,1], orders[13,9] #mins 
# ordersys.extractMinOrder() # 9
