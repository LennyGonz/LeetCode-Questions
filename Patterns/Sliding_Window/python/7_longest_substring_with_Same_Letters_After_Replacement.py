'''
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter.
Find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

def length_of_longest_substring(str1, k):
  windowStart = 0
  maxLength = 0
  maxRepeatLetterCount = 0
  frequencyMap = {}

  for windowEnd in range(len(str1)):
    rightChar = str1[windowEnd]
    if rightChar not in frequencyMap:
      frequencyMap[rightChar] = 0
    frequencyMap[rightChar] += 1

    maxRepeatLetterCount = max(maxRepeatLetterCount, frequencyMap[rightChar])

    if (windowEnd - windowStart + 1 - maxRepeatLetterCount) > k:
      leftChar = str1[windowStart]
      frequencyMap[leftChar] -= 1
      windowStart += 1
    
    maxLength = max(maxLength, windowEnd - windowStart + 1)
  
  return maxLength

def main():
  str1 = "aabccbb"
  k1 = 2
  print(length_of_longest_substring(str1, k1)) # 5 -> bc "bccbb" -> "bbbbb"

  str2 = "abbcb"
  k2 = 1
  print(length_of_longest_substring(str2, k2)) # 4 -> bc "abbcb" -> "bbbb"

  str3 = "abccde"
  k3 = 1
  print(length_of_longest_substring(str3, k3)) # 3 -> bc "abccde" -> "ccc" (by replacing the b "acccde" or the d "abccce")
  
  str4 = "ABAB"
  k4 = 2
  print(length_of_longest_substring(str4, k4))

main()
