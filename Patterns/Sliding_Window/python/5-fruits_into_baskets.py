'''
LC #904

Given an array of characters where each character represents a fruit tree, you are given two baskets, and 
Your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started.
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
------------------------------------------------------------------------------------------------------------------------------------------------------
1. First we begin with creating a frequency_map -> this controls our window size

2. When then length of the frequency map is greater than k 
    that means there is k+1 distinct characters, and we need to adjust/slide our window and
    we adjust the characters within our window so there are only k distinct characters in the window/subarray

3. However, our char_map can have multiple instances of a character so we NEED to use a while loop 
    to iteratively reduce the number of instances of a character until there are 0 instances and we can therefore remove it from the frequency_map
    * IN OTHER WORDS -> we stay in the while loop till our window contains a substring with exactly K distinct characters
    * IF our window contains a substring with more than K distinct characters, we stay in the while loop shrinking the substring, till the condition
      of having a substring with k distinct characters is met again

3. If we remove a character from the frequency_map that means there are only k distinct characters left, because prior there were K+1 characters
    So now we can proceed to adding the characters and their frequency to our map, until the condition (len(char_frequency) > k) is met again.

'''

def fruits_into_baskets(fruits):
  # start pointer
  window_start = 0
  
  # result variable
  max_fruit = 0
  
  # frequency map
  fruit_frequency = {}

  for window_end in range(len(fruits)):
    # identify the fruit we're currently on
    right_fruit = fruits[window_end]

    # populate the fruit frequency map
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # while our basket/window has more than 2 distinct fruits
    # we will reduce our window until it has only 2 distinct fruits again
    while len(fruit_frequency) > 2:
      # identify the fruit at the beginning of the window
      left_fruit = fruits[window_start]
      
      # reduce the frequency of the fruit
      fruit_frequency[left_fruit] -= 1
      
      # if the frequency of the current fruit is 0
      if fruit_frequency[left_fruit] == 0:
        # we remove it entirely from our fruit map
        del fruit_frequency[left_fruit]
      
      # we move our start pointer up
      window_start += 1
    
    # at the end of iterating OR shrinking - we update the max
    max_fruit = max(max_fruit, window_end-window_start+1)

  return max_fruit

'''
Time: O(N) - where N is all the elements in the input array, we iterate over the input array once
Space: O(N) - worst case our frequency map - holds all N elements in the input array
'''
