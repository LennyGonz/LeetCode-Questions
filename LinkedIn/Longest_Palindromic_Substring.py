'''
Expand Around Center

b a b 

1. b is the center, immidately the left pointer goes out of bounds
2. a is the center, left = b and right = b -> we have a palindrome -> if we keep expanding our pointers go out of bounds
3. b is the center, immediately the right pointer goes out of bounds

what about even string length cases?

b a a b

* logic stays the same, however our pointers can both start at the same character
one needs to start at i and the other at i + 1

We want to go through every position in the input string, and consider the character at each position to be the center of the palindrome
Once we're at that character we expand in both directions
if the character on the left and right are the same we expand
else we keep iterating through the string
'''

def longestPalindrome(s):
  res = ''
  
  resLength = 0
  
  for i in range(len(s)):
    ## odd string length case
    left = i
    right = i

    while(left >= 0 and right < len(s) and s[left] == s[right]):
      if (right-left+1) > resLength:
        res = s[left:right+1]
        resLength = right - left + 1

    # even string length case
    start = i
    end = i + 1
    
    while(start >= 0 and end < len(s) and s[start] == s[end]):
      if (end-start+1) > resLength:
        res = s[start:end+1]
        resLength = end - start + 1
  
  return res
'''
Time: O(N^2) - Since expanding a palindrome around its center could take O(N) for each input O(N) => O(N*N) = O(N^2)
Space: O(1) - Algorithm runs in constant space
'''
