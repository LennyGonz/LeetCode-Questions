def isAnagram(string1, string2):
  if len(string1) != len(string2):
    return False
  
  char_dic = {}
  
  for char in string1:
    if char not in char_dic:
      char_dic[char] = 1
    else:
      char_dic[char] += 1

  for char in string2:
    if char not in char_dic:
      return False
    
    # if this letter exceeds the count of the same letter in the first word
    # this condition is only true if we have 1 or more of the current char than string1 does of that char
    # when we hit our 3rd c (ccac) the value of char_dic['c'] = 0
    # so on our 4th iteration char_dic['c'] = 0 -- 0 < 1 #True - therefore we return False bc the current 
    elif char_dic[char] < 1:
      return False

    else:
      char_dic[char] -= 1
  
  return True

# test run this case
input1 = 'aacc'
input2 = 'ccac'
print(isAnagram(input1,input2))
