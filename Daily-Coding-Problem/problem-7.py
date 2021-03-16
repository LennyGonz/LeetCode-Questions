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

print(num_encodings('111')) # -> 3

'''
- If string starts with zero, then there's no valid encoding

- If the strings length is less than or equal to 1, there's only 1 encoding

- If the first 2 digits form a number k that is less than or equal to 26, we can recursively count the number of encodings assuming we pick k as a letter

- We can also pick the first 2 digits as a letter and count the number of encodings with this assumption

In addition, the above solution is not very efficient
Every branch calls itself recursively twice, so our runtime is O(2^n)
We can do better by using dynamic programming

All the following code does is repeat the same computation as above except starting from the base case and building up the solution
Since each iteration takes O(1), the whole algorithm now takes O(n)
'''

from collections import defaultdict

def num_encodings(s):
  # on lookup, this hashmap returns a default value of 0 if they key doesn't exist
  # cache[i] gives us # of ways to encode the substring s[i:]
  cache = defaultdict(int)
  cache[len(s)] = 1  # empty string is 1 valid encoding
  
  for i in reversed(range(len(s))):
    if s[i].startswith('0'):
      cache[i] = 0
    elif i == len(s) - 1:
      cache[i] = 1
    else:
      if int(s[i:i + 2]) <= 26:
        cache[i] = cache[i + 2]
      cache[i] += cache[i + 1]
  return cache[0]
