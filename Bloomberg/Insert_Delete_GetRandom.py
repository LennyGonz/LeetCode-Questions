'''
LeetCode #380

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

* bool insert(int val) - Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.

* bool remove(int val) - Removes an item val from the set if present. Returns true if the item was present, false otherwise.

* int getRandom() - Returns a random element from the current set of elements 
                    (it's guaranteed that at least one element exists when this method is called)
                    Each element must have the same probability of being returned

You must implement the functions of the class such that each function works in average O(1) time complexity.

input:
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]

output:
[null,true,false,true,1,true,false,2]
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Given that the functions HAVE TO run in constant time O(1)
The data structure that comes to mind is a HashMap

With a Hashmap you can Insert and Remove in constant time, and Hashmaps tell you if a value exists or not. BUT the problem is with getRandom()

With getRandom() -> we would take the indicies and generate a random value within the index range.
  - that random value is the index of the random element
  - however, hashMaps are unordered so this is the issue...
  - Since there are no indexes in hashmap, we would have to convert the hashmap keys to a list, that would take linear time. 

So we'll maintain a list of the elements aside and to use this list to compute the getRandom function

While we solved the getRandom issue between the data structures
It's also important that the data structures are both maintained simultaneously
bc when we delete an element it takes O(N) time for lists
  so instead we can do this
  --
    To delete a value at arbitrary index takes linear time. The solution here is to always delete the last value:
      * Swap the element to delete with the last one.
      * Pop the last element out.

In order to implement this strategy our hashMap needs to be the following
  - the key:value pair needs to be element:index
  - so element -> its index

Now we can maintain both data structures and do each operation in constant time
'''

from random import choice

class RandomizedSet():
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.dict = {}
    self.list = []

      
  def insert(self, val: int) -> bool:
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    # if the value is already in our data structures we don't want to add it again and RES = TRUE
    res = val not in self.dict
    
    # if the value is not in the map, then we append it to both data structures
    if res:
      self.dict[val] = len(self.list)
      self.list.append(val)
    
    # if the item IS present already, we return false
    return res

  def remove(self, val: int) -> bool:
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    """
    
    # if the value is in our dictionary, we want res=True
    res = val in self.dict
    
    # if we can remove val
    if res:
      # we need to remove it from the dictionary and the list
      # so we grab the index of the specified val
      idx = self.dict[val]
      
      # we want to swap the last element in the list, with the element we're about to remove
      # so first we grab the last element in the list
      lastVal = self.list[-1]
      
      # then we place the lsat element from the list
      # in the spot of the element we want to remove -> so instead of deleting we're just replacing
      self.list[idx] = lastVal
      
      # since we deleted "val" and swapped the last element to the index of the recently deleted
      # we need to update our list and pop the last element, bc we don't want duplicates
      self.list.pop()
      
      # since we deleted the element and swapped elements
      # we need to update the index of the element we swapped into a new index
      self.dict[lastVal] = idx
      
      # then we have to update our hashMap too, so we delete val from our hashMap
      del self.dict[val]
    
    # we return false if val IS NOT in map
    return res

  def getRandom(self) -> int:
    """
    Get a random element from the set.
    """
    return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
def main():
  obj = RandomizedSet()
  val = 1
  param_1 = obj.insert(val)
  print(obj.dict, obj.list)
  param_2 = obj.remove(val)
  print(obj.dict, obj.list)
  #param_3 = obj.getRandom()
  print(param_1)
  print(param_2)
  
main()
'''
Insert Function:
- Add value -> its index into dictionary, average O(1) time.
- Append value to array list, average O(1) time as well.

Remove Function:
- Retrieve an index of element to delete from the hashmap.
- Move the last element to the place of the element to delete, \mathcal{O}(1)O(1) time.
- Pop the last element out, \mathcal{O}(1)O(1) time.

Random Function:
- GetRandom could be implemented in \mathcal{O}(1)O(1) time with the help of standard random.choice in Python

Complexity Analysis

Time: GetRandom is always O(1). Insert and Delete both have O(1) average time complexity, and O(N) in the worst-case scenario when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.

Space complexity: O(N), to store N elements.
'''
