'''
LeetCode #217

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

-----------------------------------------------------------------------------------------------------------------------------------------

Strategy:

We iterate through the input array
  creating a frequency map of each element in the array

Then we iterate through the input array AGAIN
  however this time AS we're iterating through the array
    we check frequency value of the current element we're on
      and if that value is greater than 1, we can immediately return True
      
      ELSE
      
      we exit the 2nd for-loop without returning anything
      meaning the input array has all unique elements, so we return False - b/c no duplicates were found
'''

def containsDuplicate(nums):
  if not nums:
    return False
  
  freqMap = {}
  
  # create the frequency map
  # we iterate through the input array once
  for num in nums:
    if num not in freqMap:
      freqMap[num] = 0
    freqMap[num] += 1
  
  # iterate through the array again
  # but this time checking to see if the occurance of each num is greater than 1
  # if so we have duplicates and can return True
  for num in nums:
    if freqMap[num] > 1:
      return True
  
  # if none of the elements occured more than once
  # return False
  return False

'''
Time: O(N) - 2*N == N - double pass through input array but not nested for-loops
Space: O(N) - the hashmap will hold all N elements
'''

# PYTHON
def containsDuplicate(self, nums):
  return len(nums) > len(set(nums))
