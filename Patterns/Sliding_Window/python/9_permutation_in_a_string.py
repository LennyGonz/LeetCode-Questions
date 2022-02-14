'''
LeetCode #567. Permutation in String

Given a string and a pattern, find out if the string contains any permutation of the pattern.

We use a HashMap to remember the frequencies of all characters in the given pattern

* Our goal will be to match all the characters from this HashMap with a sliding window in the given string *

1. Create a HashMap to calculate the frequencies of all characters in the pattern.
2. Iterate through the string, adding one character at a time in the sliding window.
3. If the character being added matches a character in the HashMap, decrement its frequency in the map.
    - If the character frequency becomes zero, we got a complete match.
4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap),
    - we have gotten our required permutation and can RETURN TRUE.
5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern's size.
    - At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.
'''
def find_permutation(str1, pattern):
  windowStart = 0
  
  # we use matched to determine if we've reached the correct number of characters in pattern in the input string
  matched = 0
  
  char_frequency = {}
  
  # create a frequency map of the pattern string
  for char in pattern:
    if char not in char_frequency:
      char_frequency[char] = 0
    char_frequency[char] += 1
  
  # we begin iterating through the inputString
  for windowEnd in range(len(str1)):
    rightChar = str1[windowEnd]
    
    # if the current character we're on is in the frequency map of pattern
    if rightChar in char_frequency:
      # we decrement the frequency
      char_frequency[rightChar] -= 1
      
      # if the frequency reaches 0 - that means we've matched the number of this specific character in pattern
      # therefore we can increment matched
      if char_frequency[rightChar] == 0:
        matched += 1
    
    # if matched == len(char_frequency) - meaning all the characters and # of characters from pattern are IN the input string
    # we can return True
    if matched == len(char_frequency):
      return True

    # IF the window size is greater than the length of the pattern
    # we have to strink the window till the window matches the pattern's length
    if windowEnd >= len(pattern) - 1:
      # identify the character at the start of the window (left side)
      leftChar = str1[windowStart]
      
      # increment our starting pointer
      windowStart += 1
      
      # we ONLY care about the characters in pattern
      # so if leftChar is in the pattern frequency map
      if leftChar in char_frequency:
        # and the frequency of that character is 0
        if char_frequency[leftChar] == 0:
          # we need to reduce matched b/c our string no longer has all the characters in patter
          matched -= 1
  
  # if we iterated through the entire string and never found a permutation of patter in the inputString
  # we can return False
  return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))          # True
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))             # False
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))  # True
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))            # True


main()
