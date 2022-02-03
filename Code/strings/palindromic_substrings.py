'''
LeetCode #647

With Palindrome questions we can implement *Expand from Center* strategy

As we iterate through the string, we treat each character as the center of the palindrome
Then expand outwards and compare the strings on the opposite sides of the character

b a b     b a b       b a b
^           ^             ^
center      center        center

However, with this approach we need to consider 2 scenarios

1) Odd-length strings
2) Even-length strings

With Odd length strings we can have our 2 pointers (left and right) start by pointing at the same character
With Even length strings we NEED our 2 pointers (left and right) to start by pointing at the ith character and ith+1 character

Then expand...

Otherwise the logic remains the same
'''

def countSubStrings(s):
  res = 0
  
  for i in range(len(s)):
    # start with the odd length strings
    # our pointers will point to the same character
    left = right = i
    
    # while left is inbounds of the string and so is right
    # and left and right point to the same character -> We have a palindrome and we move our pointers
    while left >= 0 and right < len(s) and s[left] == s[right]:
      res += 1
      left -= 1
      right += 1
    
    # deal with even length strings
    left = i
    right = i + 1
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
      res += 1
      left -= 1
      right += 1
  
  return res

'''
Time: O(N)
Space: O(1)
'''

# We can also condense the code to avoid redundancy

def countPali(s, left, right):
  res = 0
  
  while left >= 0 and right < len(s) and s[left] == s[right]:
    res += 1
    left -= 1
    right += 1
  
  return res

def countSubStrings2(s):
  res = 0
  
  for i in range(len(s)):
    res += countPali(s,i,i)
    res += countPali(s,i,i+1)
  
  return res

print(countSubStrings2("aaab"))
