'''
Leetcode #1

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**************************************************************************************************************************

The strategy is to iterate through the input array

We use a hash table to store at worst-case all the elements in the inputArray
where the key is the element from the array
and the value is the corresponding index of the element (the key)

When we start iterating through the input array
We subtract the target value from the current element we're on
  and if that value is in our hash table
    we return the current element we're on AND the value that's in the hash table
  
  otherwise
    we add the current element to the hash table
'''
def twoSum(numarr, target):
  # this hash table will at worst case hold all n elements from the input array (if there are no nums that when added equal target)
  # the key = number (from input array)
  # the value = index of the number
  processedInts = {}

  # we iterate through the input array
  for index, value in enumerate(numarr):
    
    # if target-value is in our hash table - then we found the 2 numbers that when added equal the target
    if target - value in processedInts:
      # so we return the 2 indexes
      return [processedInts[target-value], index]
    else:
      # if the current number does not equal target-value
      # then we add it to the hashmap 
      processedInts[value] = index
    
  return 0

ex1 = [2, 7, 11, 15]
print(twoSum(ex1, 26))

'''
Time complexity: O(n) - We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.

Space complexity: O(n) - The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
'''
