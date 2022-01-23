'''
LeetCode #340

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

1. First we begin with creating a frequency_map -> this controls our window size

2. When then length of the frequency map is greater than k 
    that means there is k+1 distinct characters, and we need to slide our window and we
    adjust the characters within it so there are only k distinct characters in the window/subarray

3. However, our char_map can have multiple instances of a character so we NEED to use a while loop 
    to iteratively reduce the number of instances of a character until there are 0 instances and we can therefore remove it from the frequency_map
    * IN OTHER WORDS -> we stay in the while loop till our window contains a substring with exactly K distinct characters
    * IF our window contains a substring with more than K distinct characters, we stay in the while loop shrinking the substring, till the condition
      of having a substring with k distinct characters is met again

3. If we remove a character from the frequency_map that means there are only k distinct characters left, because prior there were K+1 characters
    So now we can proceed to adding the characters and their frequency to our map, until the condition (len(char_frequency) > k) is met again.

For example: "araaci", k=2

our frequency map will look like: {a:3, r:1, c:1} & window_end = 4, when we finally enter the while loop
1. First iteration we'll reduce a:3 -> a:2 BUT then we slide our window bc we need to reach a point in the window where there are only k distinct characters

2. Second iteration we'll reduce r:1 -> r:0
    NOW b/c there will no longer be any more instances of 'r' we delete it from our frequency_map,
      this breaks us from the while-loop bc now the frequency array is {a:2, c:1}

3. And the very last step is to constantly record the max_length - even when there are no duplicates to account for, we need to update the max_length,
    once we hit a duplicate we can calculate the window_size by doing (window_end-window_start+1)

So need to realize that:

(1): the frequency map controls our window_size - b/c once there are more than k distinct keys we trigger the while-loop

(2): While creating the frequency map, we're also expanding the window. Example:"araaci" -> when we add "araa" the max length is 4, once we reach the "c" we have encountered a new character and need to make adjustments to properly calculate the length of a subarray with k distinct arrays. Which is why we move the window_start pointer until we reach a character that no longer breaks the condition: len(char_frequency) > k:

(3): the while loop begins removing characters from left to right, causing the frequency map to reduce values for each key respectively, once we reach a character whose number of instances is 0 we can stop adjusting our window, because now there are only k distinct characters in it. We delete it from the map.
'''

def lengthOfLongestSubstringKDistinct(s, k):
  windowStart = 0
  char_frequency = {}
  max_length = 0
  
  for windowEnd in range(len(s)):
    rightChar = s[windowEnd]
    
    if rightChar not in char_frequency:
      # our character is the key and the frequency is the value
      char_frequency[rightChar] = 0
    char_frequency[rightChar] += 1

    # we need to be able to detect when our current substring has more than K distinct characters
    # if we take the length of the dictionary - it tells us how many keys we have aka - how many characters we have
    # REMEMBER the question says at most k distinct characters, doesnt mean we cant have more than 1 of the same character
    while len(char_frequency) > k:
      # if we entered the while-loop it's because the substring in our window has k+1 distinct characters

      # starting from the very first character in the substring (left-side) - we identify this character
      leftChar = s[windowStart]
        
      # we decrement the number of instances of this character
      char_frequency[leftChar] -= 1
        
      # if decrementing the number of instances of this character goes to 0
      if char_frequency[leftChar] == 0:
        # we delete it from our char_frequency map
        del char_frequency[leftChar]

      # we must also increment our windowStart because the beginning of this substring has changed (because we're shrinking our sliding window)
      # throughout the process of restoring the condition of having a substring with at most k distinct characters
      windowStart += 1
    
    # After we're done finding and calculating the valid substring, we must update the max_length, IF there is a new max length, else it'll stay the same
    max_length = max(max_length, windowEnd-windowStart+1)
  
  # if they ask to return the actual substring it should look something like
  # return s[windowStart:windowEnd+1]
  return max_length

'''
Time: O(N) - Where N is the number of characters in the input string

The outer for loop runs for all characters, and the inner while loop processes each character only once
therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

Space: O(K) - as we will be storing a maximum of K+1 characters in the HashMap.
'''

'''
Input: "araaci", 2

# interation 1

window_start = 0
max_length = 0
char_frequency = {}

for window_end in range(len(str1))
  right_char = str1[window_end] -> right_char = str1[0] -> right_char = a

  "a" not in {} -> True
  if right_char not in char_frequency:
    char_frequency['a'] = 0
    {a:0}
  char_frequency['a'] += 1 -> {"a": 1}

  while len(char_frequency) > k => 1 > 2 => False

  max_length = max(max_length, window_end-window_start+1) -> 0 - 0 + 1 = 1

# iteration 2

for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[1] -> right_char = 'r'

  "r" not in {a:1,} -> 
  if right_char not in char_frequency:
    char_frequency["r"] = 0
    {a:1, r:0}
  char_frequency["r"] += 1 -> {"a":1, "r":1}

  while len(char_frequency) > k => 2 > 2 => false

  max_length = max(max_length, window_end-window_start+1) -> 1 - 0 + 1 = 2

Input: "araaci", 2
# iteration 3

for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[2] -> right_char = "a"
  {'a':1,'r':1}
  if right_char not in char_frequency: => False
  char_frequency["a"] += 1 => {a:2, r:1}

  while len(char_frequency) > k: 2 > 2 => False

  max_length = max(max_length, window_end-window_start+1) -> 2 - 0 + 1 = 3

# iteration 4
for window_end in range(len(str1)):
  right_char = str1[window_end] => right_char = str1[3] => right_char = "a"

  {'a': 2, 'r': 1}
  if right_char not in char_frequency: => False
  char_frequency[right_char] += 1 => char_freqeuncy["a"] += 1 => {'a': 3, 'r': 1}

  while len(char_frequency) > k: => 2 > 2 => False

  max_length = max(max_length, window_end-window_start+1) -> 3 - 0 + 1 = 4

# iteration 5

window_start = 0
max_length = 0
char_frequency = {}

for window_end in range(len(str1))
  right_char = str1[window_end] -> right_char = str1[4] -> right_char = c

  "c" not in {} -> True
  if right_char not in char_frequency:
    char_frequency['c'] = 0
    {a:3, r:1, c:0}
  char_frequency['c'] += 1 -> {"a": 3, r: 1, c:1}

  while 3 > 2 => True
  while len(char_frequency) > k:
    left_char = str1[0] => left_char = 'a'
    char_frequency[left_char] -= 1 => char_frequency['a'] -= 1 => {a:2, r:1, c:1}
    if char_frequency[left_char] == 0: => False
    window_start += 1 => 0 + 1 = 1

    "a|r|aaci"
       ^
       window_start
  
    left_char = str1[window_start] -> left_char = str1[1] -> left_char = 'r'
    char_frequency[left_char] -= 1 -> char_frequency['r'] -= 1 => {a:2, r:0, c:1}
    if char_frequency['r'] == 0:
      del char_frequency['r']
    window_start += 1 -> 1 + 1 = 2
      "ar|a|aci"
          ^
          window_start

    # NOW we can break out of the while loop b/c the condition breaks
    # with r removed from the hash-map there are only 2-distinct chars
    
  max_length = max(max_length, window_end-window_start+1) -> max(4, 4-2+1) -> max(4,3) = 4

Input: "araaci", 2

# iteration 6

  for window_end in range(len(str1)):
    right_char = str1[window_end] -> right_char = str1[5] -> right_char = i

    "i" not in {} -> True
    if right_char not in char_frequency:
      char_frequency['i'] = 0
      {a:3, r:1, c:1, i:0}
    char_frequency['c'] += 1 -> {a: 2, r: 1, c:1, i:1}

    while len(char_frequency) > k:
      left_char = str1[window_start] -> left_char = str1[2] -> left_char = 'a'
      char_frequency[left_char] -= 1 -> char_frequency['a'] -= 1 => {a:1, c:1, i:1}
      if char_frequency['a'] == 0: # False
      window_start += 1 -> 2 + 1 = 3

      "ara|a|ci"
           ^
           window_start
    
    while len(char_frequency) > k:
      left_char = str1[window_start] -> left_char = str1[3] -> left_char = 'a'
      char_frequency[left_char] -= 1 -> char_frequency['a'] -= 1 => {a:0, c:1, i:1}
      if char_frequency['a'] == 0:
        del char_frequency['a'] -> {c:1, i:1}
      window_start += 1 -> 3 + 1 = 4
    
      "araa|c|i"
            ^
            window_start
    
    max_length = max(max_length, window_end-window_start+1) -> max(4, 5-4+1) -> max(4,2) = 4

# iteration 7

We break out of the for-loop & return max_length = 4
'''

print(lengthOfLongestSubstringKDistinct("araaci", 2))
print(lengthOfLongestSubstringKDistinct("araaci", 1))
print(lengthOfLongestSubstringKDistinct("cbbebi", 3))


def lengthOfLongestSubstringKDistinct(s, k):
  windowStart = 0
  char_frequency = {}
  max_length = 0
    
  for windowEnd in range(len(s)):
    rightChar = s[windowEnd]
    
    if rightChar not in char_frequency:
      # our character is the key and the frequency is the value
      char_frequency[rightChar] = 0
    char_frequency[rightChar] += 1
  
    # we need to be able to detect when our current substring has more than K distinct characters
    # if we take the length of the dictionary - it tells us how many keys we have aka - how many characters we have
    # REMEMBER the question says at most 2 distinct characters, doesnt mean we cant have more than 1 of the same character
    while len(char_frequency) > k:
      # if we entered the while-loop it's because the substring in our window has k+1 distinct characters
      
      # starting from the very first character in the substring (left-side) - we identify this character
      leftChar = s[windowStart]
      
      # we decrement the number of instances of this character
      char_frequency[leftChar] -= 1
      
      # if decrementing the number of instances of this character goes to 0
      if char_frequency[leftChar] == 0:
        # we delete it from our char_frequency map
        del char_frequency[leftChar]

      # we must also increment our windowStart because the beginning of this substring has changed
      # throughout the process of restoring the condition of having a substring with at most k distinct characters
      windowStart += 1
    
    # After we're done finding and calculating the valid substring, we must update the max_length, IF there is a new max length, else it'll stay the same
    max_length = max(max_length, windowEnd-windowStart+1)
  
  return max_length
