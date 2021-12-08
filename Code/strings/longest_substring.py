def lengthOfLongestSubstring(string):
  '''
  Time: O(n)
  Space: O(k)
  '''
  longest = 0
  left, right = 0, 0
  chars = set()

  while left < len(string) and right < len(string):
    if string[right] not in chars:
      chars.add(string[right])
      right += 1
      longest = max(longest, right - left)
    
    else:
      chars.remove(string[left])
      left += 1
  return longest

input1 = "abcabcbb"
print(lengthOfLongestSubstring(input1))

'''
Given a string s, find the length of the longest substring without repeating characters.
'''
def length_of_longest_substring(string):
  windowStart = 0
  maxLength = 0
  char_map = {}
  
  for windowEnd in range(len(string)):
    rightChar = string[windowEnd]
    
    if rightChar in char_map:
      windowStart = max(windowStart, char_map[rightChar]+1)
    
    char_map[rightChar] = windowEnd
    
    maxLength = max(maxLength, windowEnd-windowStart+1)
  
  return maxLength

input2 = "abcabcbb"
print(length_of_longest_substring(input2))
