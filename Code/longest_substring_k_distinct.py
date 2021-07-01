def longestSubstring(str1, k):
  window_start = 0
  max_length = 0
  char_freq = {}

  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in char_freq:
      char_freq[right_char] = 0
    char_freq[right_char] += 1

    while len(char_freq) > k:
      left_char = str1[window_start]
      char_freq[left_char] -= 1
      if char_freq[left_char] == 0:
        del char_freq[left_char]
      window_start += 1
    
    max_length = max(max_length, window_end-window_start+1)
  
  return max_length

print(longestSubstring("araaci", 2))
