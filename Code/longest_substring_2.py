def lengthOfLongestSubstring(s):
  start = 0
  maxLength = 0
  usedChar = {}

  for index, char in enumerate(s):
    print("index",index, '||', "char", char)
    if char in usedChar and start <= usedChar[char]:
      print("start", start, "||", "usedChar[char]", usedChar[char])
      start = usedChar[char] + 1
      print("Updated start", start)
    else:
      maxLength = max(maxLength, index - start + 1)
      print("maxLenfth", maxLength)
    print("")
    print("char - value", char, '||', "key of this char", index)
    usedChar[char] = index
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  
  for key, value in usedChar.items():
    print("key:", key, "||", "value", value)
  return maxLength

#tmmzuxta cause we didnt update start
#abcabcbb
print(lengthOfLongestSubstring("tmmzuxta"))


#####################################################################################
# this example demonstrates the need for the additional condition of `start <= usedChar[char]`
'''
def lengthOfLongestSubstring(s):
  start = 0
  maxLength = 0
  usedChar = {}

  for index, char in enumerate(s):
    print("index",index, '||', "char", char)
    if char in usedChar: # and start <= usedChar[char] ## by not adding the 2nd conditional we never update `start` which we use to correctly calculuate maxlength
      print("start", start, "||", "usedChar[char]", usedChar[char])
      start = usedChar[char] + 1
      print("Updated start", start)
    else:
      maxLength = max(maxLength, index - start + 1)
      print("maxLenfth", maxLength)
    print("")
    print("char - value", char, '||', "key of this char", index)
    usedChar[char] = index
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  
  for key, value in usedChar.items():
    print("key:", key, "||", "value", value)
  return maxLength

#tmmzuxta cause we didnt update start
#abcabcbb
print(lengthOfLongestSubstring("tmmzuxta"))
'''
#####################################################################################
