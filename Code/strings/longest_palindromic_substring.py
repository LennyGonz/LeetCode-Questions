'''
LeetCode #5

The Strategy is: Expand Around Center

b a b 

1. b is the center, immidately the left pointer goes out of bounds
2. a is the center, left = b and right = b -> we have a palindrome -> if we keep expanding our pointers go out of bounds
3. b is the center, immediately the right pointer goes out of bounds

what about even string length cases?

b a a b

* logic stays the same, however our pointers can both start at the same character
one needs to start at i and the other at i + 1

1. We want to go through every position in the input string, and consider the character at each position to be the center of the palindrome
2. Once we're at that character we expand in both directions
3. if the character on the left and right are the same we expand
4. else we keep iterating through the string
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

def longestPalindrome(s):
  if not s:
    return 0

  size = len(s)
  table, longest_start, longest_end = [[False] * size for _ in range(size)], None, None

  # one letter is palindrome
  for i in range(size):
    table[i][i] = True

  # start from 2-letter words, then 3-letter, etc
  for l in range(2, size + 1):
    for start in range(size - l + 1):
      end = start + l - 1
      is_equal_letters = s[start] == s[end]
      table[start][end] = is_equal_letters if l == 2 else is_equal_letters and table[start + 1][end - 1]
      if table[start][end]: # update longest palindrome
        longest_start, longest_end = start, end

  return s[longest_start:longest_end + 1] if longest_start is not None else s[0]


'''
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
input1="babad"
print(longestPalindrome(input1))

'''
Time: O(n^2)
Space: O(n^2)
'''
