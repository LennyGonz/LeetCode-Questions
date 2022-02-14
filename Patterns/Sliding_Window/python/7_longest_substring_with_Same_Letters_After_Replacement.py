'''
LeetCode #424. Longest Repeating Character Replacement

Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter.
Find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

The Sliding Window Adjustment NEEDS to be dynamic -> just like in Longest SubString With Distinct Characters

1. We can use a HashMap to count the frequency of each letter.
2. We will iterate through the string to add one letter at a time in the window.
3. We will also keep track of the count of the MAXIUMUM REPEATING LETTER in any window (let's call it maxRepeatLetterCount).
4. So, at any time, we know that have a window with one letter repeating maxRepeatLetterCount times
    - THIS MEANS we should try to replace the remaining letters.
      - if the remaining letters are less than or equal to k, we can replace them all.
      - if we have more than k remaining letters, we should shrink the window as we cannot replace more than k letters.

5. While shrinking the window, we don't need to update maxRepeatLetterCount (hence, it represents the maximum repeating count of ANY letter for ANY window).
    -Why don't we need to update this count when we shrink the window?
      - Since we have to replace all the remaining letters to get the longest substring having the same letter in any window,
        - we can't get a better answer from any other window even though,
            all occurrences of the letter with frequency maxRepeatLetterCount is not in the current window
'''

def length_of_longest_substring(str1, k):
  # start pointer
  windowStart = 0
  
  # will hold the length of the longest substring
  maxLength = 0
  
  # will hold the max frequency of a single character in the substring
  maxRepeatLetterCount = 0
  
  # hashMap to count the frequency of each letter in the inputString
  frequencyMap = {}

  # we iterate through the inputString
  for windowEnd in range(len(str1)):
    # identify the current character in the string
    rightChar = str1[windowEnd]
    
    # if the current character is NOT in the hashMap - add it
    if rightChar not in frequencyMap:
      frequencyMap[rightChar] = 0
    
    # if it is - increment the frequency by 1
    frequencyMap[rightChar] += 1

    # determine what is the highest frequency of a character
    maxRepeatLetterCount = max(maxRepeatLetterCount, frequencyMap[rightChar])

    # We know that maxRepeatLetterCount - holds the integer value of the maximum frequency of a character in the current substring our window holds
    # SO
    # we take the size of the window and SUBTRACT THAT SIZE from maxRepeatLetterCount
    # THIS MEANS we should try to replace the remaining letters.
      # if we have more than k remaining letters, we should shrink the window as we cannot replace more than k letters.
    if (windowEnd - windowStart + 1 - maxRepeatLetterCount) > k:
      # here we need to adjust our window, bc there are more distinct characters
      # than repeated characters, and we cant replace them all!
      # so we make our window smaller, which means we need to correctly edit our
      # frequency map to correctly depict what's inside our window
      leftChar = str1[windowStart]
      frequencyMap[leftChar] -= 1
      windowStart += 1

    # We just shrunk our window - so now we must calculate if the length is greater than the current maxLength
    # another case is
    # If the remaining letters are less than or equal to k, we can replace them all - in which case we'll calculate maxLength here
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
