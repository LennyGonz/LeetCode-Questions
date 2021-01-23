'''
Time: O(n)
Space: O(n)
'''

def is_valid(string):
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}
  
  for char in string:
    if char in mapping:
      if stack:
        top_element = stack.pop()
      else:
        top_element = '#'
    
      if mapping[char] != top_element:
        return False
    
    else:
      stack.append(char)
  
  return not stack

input1 = '([{}])'
print(is_valid(input1))
input2 = '((([{}])'
print(is_valid(input2))
input3 = '(()'
print(is_valid(input3))
