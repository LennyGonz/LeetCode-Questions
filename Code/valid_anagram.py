def isAnagram(s, t):
  if len(s) != len(t):
    return False
  
  char_dic = {}
  
  for index, char in enumerate(s):
    print('index', index, '||', 'char', char)
    if char not in char_dic:
      char_dic[char] = 1
    else:
      char_dic[char] += 1
  
  d_items = char_dic.items()

  for item in d_items:
    print(item)
  
  for char in t:
    if char not in char_dic:
      return False
    
    # if this letter exceeds the count of the same letter in the first word
    elif char_dic[char] < 1:
      return False

    else:
      char_dic[char] -= 1
  
  return True

# test run this case
input1 = 'aacc'
input2 = 'ccac'
print(isAnagram(input1,input2))
