'''
LeetCode #186. Reverse Words in a String II - Microsoft & Salesforce & Amazon

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

To have this problem in Amazon interview is a good situation, since input is a mutable structure and
  hence one could aim O(1) space solution without any technical difficulties.

* The idea is simple: reverse the whole string and then reverse each word *

Strategy:
Let's first implement two functions:

1. reverse(l: list, left: int, right: int), which reverses array characters between left and right pointers.

2. reverse_each_word(l: list), which uses two pointers to mark the boundaries of each word and previous function to reverse it.

Now reverseWords(s: List[str]) implementation is straightforward:

- Reverse the whole string: reverse(s, 0, len(s) - 1).

- Reverse each word: reverse_each_word(s).
'''

# Solution 1
def reverse(l, left, right):
  while left < right:
    l[left], l[right] = l[right], l[left]
    left, right = left + 1, right - 1

def reverse_each_word(l):
  n = len(l)
  start = end = 0
  
  while start < n:
    # go to the end of the word
    while end < n and l[end] != ' ':
      end += 1
    # reverse the word
    reverse(l, start, end - 1)
    # move to the next word
    start = end + 1
    end += 1

# main function
def reverseWords(s):
  """
  Do not return anything, modify s in-place instead.
  """
  # reverse the whole string
  reverse(s, 0, len(s) - 1)
  
  # reverse each word
  reverse_each_word(s)
'''
Time: O(N), it's two passes along the string
Space: O(1), it's a constant space solution
'''

# Solution 2
def reverseWords(s):
  def swapChars(i, j): 
    #go through and reverse until middle
    while i < j:
      s[i], s[j] = s[j], s[i] #swap
      i+=1
      j-=1
  
  #first use func to swap whole arr
  swapChars(0, len(s) - 1)
  
  #now go and just reverse each word individually
  i = 0
  j = 0
  while i < len(s):
    j = i #reset j to start at i
    while j < len(s) and s[j] != " ": #keep searching for next space or go out of bounds
      j += 1
    swapChars(i, j-1) #swap at j-1 not j, since j is out of bounds or a " "
    i = j + 1 #inc i to point to after space
