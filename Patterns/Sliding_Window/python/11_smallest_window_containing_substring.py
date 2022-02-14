'''
LeetCode #76 - Minimum Window Substring

In any sliding window based problem we have two pointers.

One right pointer whose job is to expand the current window and then
we have the leftt pointer whose job is to shrink a given window. 
  - At any point in time only ONE of these pointers MOVES and 
  - the other ONE remains FIXED.

1. We keep expanding the window by moving the right pointer. 
2. WHEN the window has ALL the desired characters, we shrink (if possible) and save the smallest window till now.



We will keep track of all the words in a HashMap and try to match them in the given string. Here are the set of steps for our algorithm:

1. Keep the frequency of every word in a HashMap.
2. Starting from every index in the string, try to match all the words.
3. In each iteration, keep track of all the words that we have already seen in another HashMap.
4. If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
5. Store the index if we have found all the words.

***********************************************************************************************************************************************

1. We start with two pointers, left and right initially pointing to the first element of the string SS.

2. We use the rightright pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of TT.

3. Once we have a window with all the characters, we can move the left pointer ahead one by one.
    - If the window is still a desirable one we keep on updating the minimum window size.

4. If the window is not desirable any more, we repeat step2 and step3.

'''
def find_substring(string, pattern):
  # start pointer
  windowStart = 0
  
  # this variable will help is keep track that we're matching the correct number
  # of characters in the given pattern
  matched = 0
  
  # marks the beginning of the substring in the current minimal window
  substr_start = 0
  
  # keeps track of the length of the window
  minLength = len(string) + 1
  
  # hashMap that we'll map the pattern string
  char_frequency = {}
  
  # populate the hashMap with the characters in the pattern string
  for char in pattern:
    if char not in char_frequency:
      char_frequency[char] = 0
    char_frequency[char] += 1

  # we iterate over the inputString, position by position
  for windowEnd in range(len(string)):
    # identify the current character we're on
    rightChar = string[windowEnd]
    
    # if the character is in pattern frequency map
    if rightChar in char_frequency:
      # reduce the number of instances by 1
      char_frequency[rightChar] -= 1
      if char_frequency[rightChar] >= 0:
        matched += 1
    
    # if we have the matching amount of characters in our current substring as the pattern string
    # that means we have a valid substring - and now we want to try and shrink it as much as possible
    # while still containing all the characters in the pattern
    while matched == len(pattern):
      # if the current minLength is greater than the current minLength
      # then we can update the size
      if minLength > windowEnd - windowStart + 1:
        # update the new minLength
        minLength = windowEnd - windowStart + 1
        # identify the start of the substring
        substr_start = windowStart
      
      leftChar = string[windowStart]
      windowStart += 1
      
      # if while shrinking the substring we remove a chacater thats part of the pattern
      # we need to add 1 back to its frequency
      # and redue matched IF the frequency of that character is 0
      # bc then we no longer have a valid substring
      if leftChar in char_frequency:
        if char_frequency[leftChar] == 0:
          matched -= 1
        char_frequency[leftChar] += 1
  
  # if we iterated through the entire string
  # and didnt find a VALID substring
  # we return an empty string
  if minLength > len(string):
    return ''

  return string[substr_start : substr_start + minLength]

def main():
  print(find_substring("aabdecz", "abc")) # abdec
  print(find_substring("abdbca", "abc")) # bca
  print(find_substring("adcad", "abc")) # 
  print(find_substring("aaaaaabcd", "abc"))

main()
