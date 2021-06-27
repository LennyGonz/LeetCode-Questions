def count_invalid_parenthesis(string):
  opened = 0
  invalid = 0
  for c in string:
    if c == '(':
      opened += 1
    elif c == ')':
      if opened > 0:
        opened -= 1
      else:
        invalid += 1
  # Count as invalid all unclosed parenthesis
  invalid += opened
  return invalid
