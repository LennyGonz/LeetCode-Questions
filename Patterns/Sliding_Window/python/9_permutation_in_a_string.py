def find_permutation(str1, pattern):
  windowStart = 0
  matched = 0
  char_frequency = {}
  
  for char in pattern:
    if char not in char_frequency:
      char_frequency[char] = 0
    char_frequency[char] += 1
  
  for windowEnd in range(len(str1)):
    rightChar = str1[windowEnd]
    if rightChar in char_frequency:
      char_frequency[rightChar] -= 1
      if char_frequency[rightChar] == 0:
        matched += 1
    
    if matched == len(char_frequency):
      return True

    if windowEnd >= len(pattern) - 1:
      leftChar = str1[windowStart]
      windowStart += 1
      if leftChar in char_frequency:
        if char_frequency[leftChar] == 0:
          matched -= 1
    
  return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))          # True
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))             # False
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))  # True
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))            # True


main()
