'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
'''

def num_encodings(string):
  if string.startswith('0'):
    return 0
  elif len(string) <= 1:
    return 1
  
  total = 0

  if int(string[:2]) <= 26:
    total += num_encodings(string[2:])
  
  total += num_encodings(string[1:])

  return total

print(num_encodings('111'))

'''
- If string starts with zero, then there's no valid encoding

- If the strings length is less than or equal to 1, there's only 1 encoding

- If the first 2 digits form a number k that is less than or equal to 26, we can recursively count the number of encodings assuming we pick k as a letter

- We can also pick the first 2 digits as a letter and count the number of encodings with this assumption
'''
