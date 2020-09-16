'''
Time: O(n^2)
Space: O(n^2)
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
