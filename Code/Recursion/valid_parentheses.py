def isValid(s):
  opening_brackets = []
  open_to_close = {'(':')', '[':']', '{':'}'}
  
  for char in s:
    # If we encounter an opening character append it to the stack
    if char in open_to_close:
      opening_brackets.append(char)
    
    # if our stack is NOT empty -> we don't have valid pairs
    elif not opening_brackets:
      return False
    
    else:
      opening = opening_brackets.pop()
      closing = open_to_close[opening]
      
      if char != closing:
        return False
    
  return not opening_brackets

example = "({[]})()"
print(isValid(example))
