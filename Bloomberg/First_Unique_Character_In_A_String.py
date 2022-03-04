'''
LeetCode #387

Given a string s, find the first non-repeating character in it and return its index.

If it does not exist, return -1.

Input: s = "loveleetcode"
Output: 2

Of course we need to traverse the string, but what I want to do first is
create a frequency map -> iterate over the string and count all the occurances of each character
the character is the key and the value is the # of occurances of that character

Then we iterate over the string again
  and for each character in the string we use the current character we're on to check its frequency
    and whichever character returns a frequency of 1 first
      we return its index
'''

def firstUniqChar(string):
  stringMap = {}
  
  # create the frequency map
  for char in string:
    if char not in stringMap:
      stringMap[char] = 0
    stringMap[char] += 1
  
  # iterate over the string -> looking for the first character with only 1 occurance
  for index,char in enumerate(string):
    if stringMap[char] == 1:
      return index

  return -1

'''
Time complexity : O(N) since we go through the string of length N two times.
Space complexity: O(1) because English alphabet contains 26 letters.
'''
