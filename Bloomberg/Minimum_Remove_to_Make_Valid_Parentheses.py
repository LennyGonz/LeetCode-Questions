'''
Leetcode #1249

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
-------------------------------------------------------------------------------------------

Before removing any parenthesis, we need to create a balanced/valid string,
  in Balance Parenthesis we keep track of a variable balance, we add 1 for every '(' and subtract 1 for every ')'
    at the end Balance should be 0, any other value -> we have an unbalanced string

Each ")" was paired with the closest "(" that isn't already paired, how do we do this in code? We need to know the indexes of the problematic "(".

We use a stack. 
  Each time we see a "(", we should add its index to the stack.
  Each time we see a ")", we should remove an index from the stack because the ")" will match with whatever "(" was at the top of the stack.
    The length of the stack is equivalent to the balance
  
  We need to do the following:
    - Remove a ")" if it is encountered when stack was already empty (prevent negative balance).
    - Remove a "(" if it is left on stack at end (prevent non-zero final balance).

So in code:
1. Convert string to list, because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
2. Iterate through list
3. Keep track of indices with open parentheses in the stack.
    - In other words, when we come across open parenthesis we add the corresponding index to the stack.
4. When we come across close parenthesis we pop an element from the stack.
    - If the stack is empty we replace current list element with an empty string
5. After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
6. Convert list to string and return
'''

def minRemoveToMakeValid(s):
  s = list(s)
  stack = []
  for index, char in enumerate(s):
    if char == '(':
      stack.append(index)
    elif char == ')':
      if stack:
        stack.pop()
      else:
        s[index] = ''

  while stack:
    s[stack.pop()] = ''

  return ''.join(s)

'''
Time complexity - O(n), where n is the length of the input string
Memory complexity - O(n), we use a list, which could have up to n characters in them, and thus require up to O(n) space.
'''

def main():
  print(minRemoveToMakeValid("lee(t(c)o)de)"))

main()

