def find_substring(string, pattern):
  windowStart = 0
  matched = 0
  substr_start = 0
  minLength = len(string) + 1
  
  char_frequency = {}
  
  for char in pattern:
    if char not in char_frequency:
      char_frequency[char] = 0
    char_frequency[char] += 1

  for windowEnd in range(len(string)):
    rightChar = string[windowEnd]
    
    if rightChar in char_frequency:
      char_frequency[rightChar] -= 1
      if char_frequency[rightChar] >= 0:
        matched += 1
    
    while matched == len(pattern):
      if minLength > windowEnd - windowStart + 1:
        minLength = windowEnd - windowStart + 1
        substr_start = windowStart
      
      leftChar = string[windowStart]
      windowStart += 1
      
      if leftChar in char_frequency:
        if char_frequency[leftChar] == 0:
          matched -= 1
        char_frequency[leftChar] += 1
  
  if minLength > len(string):
    return ''

  return string[substr_start : substr_start + minLength]

def main():
  print(find_substring("aabdecz", "abc")) # abdec
  print(find_substring("abdbca", "abc")) # bca
  print(find_substring("adcad", "abc")) # 

main()
