'''
LeetCode #1209

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
Causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

----------------------------------------------------------------------------------------------------------------------------------------------
Bruteforce:

1) we iterate over the string comparing K-letters at a time
    - we have an empty string where we add all the elements that weren't K-adjacent initially

2) then we iterate over the new string and repeat the process till there are no more k-adjacent duplicates

* but this is very inefficent

----------------------------------------------------------------------------------------------------------------------------------------------
Optimal:

I can use a stack to keep track of all the characters and the number of occurances -> [(character, frequency)]

How I plan on doing this:

I iterate through the string -> character by character

We add each character to the stack
  - if the character is already in the stack we increment the frequency by 1
  - else the character is NOT in the stack we append to the stack and initialize the frequency to 1
  - if the frequency of the current character reaches k
    - we just pop the character from the stack

* We cannot use a dictionary(frequency map) because the order of the character matters & dictionaries DO NOT maintain order

Once we're done iterating over the input string
we can loop through our stack and create the string and return it

Time: O(N) - we iterate through the string once - where N is the total number of characters in the input string
Space: O(N) - worst case the stack holds all the characters in the input string (there are no duplicates)
'''

def removeDuplicates(string, k):
  # we use this stack to keep track of each character and the # of occurances
  stack = []
  
  for char in string:
    # if the stack is NOT empty AND
    # the top element of the stack is the SAME as the current character
    # we increase the freqeuncy of the character by 1
    if stack and stack[-1][0] == char:
      stack[-1][1] += 1
    
    # if the current character is NOT in the stack
    # we append it to the stack
    else:
      stack.append([char,1])
    
    # if the frequency of the character at the top of the stack is K
    # then we must remove it - so we pop it from the stack
    if stack[-1][1] == k:
      stack.pop()
  
  # once we're done iterating over the input string
  # we create the string -> "a" * 2 = "aa"
  return ''.join(char * freq for char, freq in stack)

def main():
  str1 = "abcd"
  str2 = "deeedbbcccbdaa"
  str3 = "pbbcggttciiippooaais"
  
  k1 = 2
  k2 = 3
  k3 = 2
  
  print(removeDuplicates(str1, k1)) # "abcd"
  print(removeDuplicates(str2, k2)) # "aa"
  print(removeDuplicates(str3, k3)) # "ps"

main()
