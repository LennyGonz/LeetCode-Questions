def find_string_anagrams(string, pattern):
  windowStart = 0
  matched = 0
  char_frequency = {}
  
  for char in pattern:
    if char not in char_frequency:
      char_frequency[char] = 0
    char_frequency[char] += 1
  
  result_indices = []
  
  for windowEnd in range(len(string)):
    rightChar = string[windowEnd]
    if rightChar in char_frequency:
      char_frequency[rightChar] -= 1
      if char_frequency[rightChar] == 0:
        matched += 1
    
    if matched == len(char_frequency):
      result_indices.append(windowStart)
    
    if windowEnd >= len(pattern) - 1:
      leftChar = string[windowStart]
      windowStart += 1
      
      if leftChar in char_frequency:
        if char_frequency[leftChar] == 0:
          matched -= 1
        char_frequency[leftChar] += 1
  
  return result_indices

def main():
  print(find_string_anagrams("ppqp", "pq")) # [1,2]
  print(find_string_anagrams("abbcabc", "abc")) #[2,3,4]


main()
