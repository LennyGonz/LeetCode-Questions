def isAnagram(s, t):
  if len(s) != len(t):
    return False
  
  char_dic = {}
  
  for char in s:
    if char not in char_dic:
      char_dic[char] = 1
    else:
      char_dic[char] += 1
  
  d_items = char_dic.items()

  for item in d_items:
    print(item)
  
  for char in t:
    print("current char:", char)
    if char not in char_dic:
      return False
    
    # if this letter exceeds the count of the same letter in the first word
    # when we hit our 3rd c (ccac) the value of char_dic['c'] = 0 -- meaning we have 1 more c in string t than we did in string s
    elif char_dic[char] < 1:
      return False

    else:
      print("Before -> char_dic[char]=",char_dic[char])
      char_dic[char] -= 1
      print("After -> char_dic[char]=",char_dic[char])
      
  
  return True

# test run this case
input1 = 'aacc'
input2 = 'ccac'
print(isAnagram(input1,input2))
