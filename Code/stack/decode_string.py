'''
# LeetCode Question 394

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 

Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.

For example, there will not be input like 3a or 2[4].

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

The idea is to seperate the number and the character
We can do this by iterating through the string and appending every character to our stack UNLESS it is a closing bracket
  - we don't want to append the closing bracket bc that's the character we'll use to stop and transform 3[a] into "aaa"
  
  so when we do reach a closing bracket - we stop appending to the stack
  AND
  we start popping what's on the stack - what should be at the top of the stack is a character - and we stop popping till we hit the opening bracket
    so we have a variable that we initiate as an empty string - this will hold our decrypted string
    our variable will hold this string
  since we stopped popping when we hit an opening bracket we will need to do a single pop
  
  Once the single pop is done - what's left is an integer
  Since our input is a string - we will need to cast our string into an integer - however the integer could be double/triple digits
    so while the char is a digit we keep popping and rebuilding the integer
  when we finally created the integer we cast it from a string to integer and multiply the char by the integer (3[a] -> 3*a = aaa)
  then we add "aaa" back onto the stack
  
  We repeat this process until we've finished iterating over the entire string
  And our return statement -> we join everything inside the stack
'''

def decodeString(s):
  stack = []
  
  for i in range(len(s)):
    # we want to iterate through the entire input string and add it to the stack UNLESS it's a closing bracket
    if s[i] != "]":
      stack.append(s[i])

    # If we have reach a closing bracket we can start to decode
    else:
      substr = ""
      
      # while the element at the top of the stack IS NOT an opening bracket, continue popping elements and contrusting the substring
      while stack[-1] != "[":
        substr = stack.pop() + substr
      
      # We need to remove the opening bracket from our stack because
      # 1) we only needed it as a marker to stop from constructing the substring within the brackets
      # 2) we want the integer that tells us how many times to multiply the substring by
      stack.pop()
      
      # We need to start constructing the integer
      k = ""
      
      while stack and stack[-1].isdigit():
        k = stack.pop() + k
      
      # We NOW have our integer AND the substring within a bracket pair so, lets add it and continue decoding the inner substrings
      stack.append(int(k) * substr)
  
  return "".join(stack)

'''
Time: O(k * n) - We traverse a string of size n and iterate k times to decode each pattern of form k[string]
Space: O(m+n) - where m is the number of letters(a-z) and n is the number of digits(0-9) in string s
'''


print(decodeString("3[a]2[bc]")) # "aaabcbc"
print()
print(decodeString("3[a2[c]]")) # "accaccacc"
print()
print(decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
print()
print(decodeString("abc3[cd]xyz")) # "abccdcdcdxyz"
