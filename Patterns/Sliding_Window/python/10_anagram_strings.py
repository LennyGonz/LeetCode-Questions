'''
LeetCode #438. Find All Anagrams in a String

Given a string and a pattern, find all anagrams of the pattern in the given string.
Return an array of all the start indices of pattern's anagrams in the given string

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

- patterns are known in advance, and the set of characters in the patterns is very limited as well:
  - 26 lowercase English letters. 
  - Hence one could allocate array or hashmap with 26 elements and use it as a letter counter in the sliding window

- We need to find every occurrence of any permutation of the pattern in the string. 
- We will use a list to store the starting indices of the anagrams of the pattern in the string.

'''

def find_string_anagrams(str1, pattern):
  # we'll use matched as a way to determine when we
  # have all the characters in pattern in the substring contained in the sliding window
  window_start, matched = 0, 0
  result_indices = []
  char_frequency = {}

  # we create a frequency map for the characters in pattern
  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    # identify the current character
    right_char = str1[window_end]
    
    # if the current character is in pattern's frequency map
    if right_char in char_frequency:
      # Decrement the frequency of matched character
      char_frequency[right_char] -= 1
      
      # AND IF the frequency of the current character is 0
      # then we can increment matched - thats to say the substring we have in our window
      # contains the same amount of the current character as the pattern does
      if char_frequency[right_char] == 0:
        matched += 1

    # if matched == len(char_frequency) -> then we have an anagram and we can append the indice
    if matched == len(char_frequency):  # Have we found an anagram?
      result_indices.append(window_start)

    # if our window contains a substring bigger than the pattern
    # we have to shrink the substring
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      
      # however if the character we're about to chop off is in the pattern hashmap
      # we need to increment the frequency
      # and reduce matched - bc our substring no longer contains the anagram
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        char_frequency[left_char] += 1  # Put the character back

  return result_indices

'''
Time Complexity: O(N+M) - where 'N' and 'M' are the number of characters in the input string and the pattern respectively.

Space Complexity: O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap.
  - In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.
'''

def main():
  print(find_string_anagrams("ppqp", "pq")) # [1,2]
  print(find_string_anagrams("abbcabc", "abc")) #[2,3,4]
  print(find_string_anagrams("cbaebabacd","abc"))


main()
