'''
LeetCode #159

We can use a HashMap to remember the frequency of each character we have processed

1. First, we will insert characters from the beginning of the string until we have K distinct characters in the HashMap.

2. These characters will constitute our sliding window. 
  We are asked to find the longest such window having no more than 2 distinct characters.
  We will remember the length of this window as the longest window so far.

3. After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.

  In each step, we will try to shrink the window from the beginning
    IF the count of distinct characters in the HashMap is larger than K. 
  
    We will shrink the window UNTIL we have no more than 2 distinct characters in the HashMap.
    This is needed as we intend to find the longest window.
    
4. While shrinking, we'll decrement the character's frequency going out of the window and 
    remove it from the HashMap if its frequency becomes zero.
    
5. At the end of each step, we'll check if the current window length is the longest so far, and if so, remember its length.
'''

def lengthOfLongestSubstringKDistinct(s):
  windowStart = 0
  char_frequency = {}
  max_length = 0
  
  for windowEnd in range(len(s)):
    rightChar = s[windowEnd]
    
    if rightChar not in char_frequency:
      # our character is the key and the frequency is the value
      char_frequency[rightChar] = 0
    char_frequency[rightChar] += 1

    # we need to be able to detect when our current substring has more than K distinct characters
    # if we take the length of the dictionary - it tells us how many keys we have aka - how many characters we have
    # REMEMBER the question says at most 2 distinct characters, doesnt mean we cant have more than 1 of the same character
    while len(char_frequency) > 2:
      # if we entered the while-loop it's because the substring in our window has k+1 distinct characters

      # starting from the very first character in the substring (left-side) - we identify this character
      leftChar = s[windowStart]
        
      # we decrement the number of instances of this character
      char_frequency[leftChar] -= 1
        
      # if decrementing the number of instances of this character goes to 0
      if char_frequency[leftChar] == 0:
        # we delete it from our char_frequency map
        del char_frequency[leftChar]

      # we must also increment our windowStart because the beginning of this substring has changed (because we're shrinking our sliding window)
      # throughout the process of restoring the condition of having a substring with at most k distinct characters
      windowStart += 1
    
    # After we're done finding and calculating the valid substring, we must update the max_length, IF there is a new max length, else it'll stay the same
    max_length = max(max_length, windowEnd-windowStart+1)
  
  # if they ask to return the actual substring it should look something like
  # return s[windowStart:windowEnd+1]
  return max_length

'''
Time: O(N) - Where N is the number of characters in the input string

The outer for loop runs for all characters, and the inner while loop processes each character only once
therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

Space: O(K) - as we will be storing a maximum of K+1 characters in the HashMap.
'''
