'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

Here we can continue following our sliding window pattern

But first we begin with creating a frequency_map -> this controls our window size

When then length of the frequency map is greater than k 
that means there is k+1 distinct characters, and we need to slide our window and adjust the characters within it so there are only k distinct characters in the window/subarray

However, our char_map can have multiple instances of a character so we NEED to use a while loop to iteratively reduce the number of instances of a character until there are 0 instances and we can therefore remove it from the frequency_map

If we remove a character from the frequency_map that means there are only k distinct characters left, because prior there were K+1 characters
So now we can proceed to adding the characters and their frequency to our map, until the condition (len(char_frequency) > k) is met again.

For example: "araaci", 2

our frequency map will look like: {a:3, r:1, c:1} & window_end = 4, when we finally enter the while loop
First iteration we'll reduce a:3 -> a:2 BUT then we slide our window bc we need to reach a point in the window where there are only k distinct characters
Second iteration we'll reduce r:1 -> r:0 NOW b/c there will no longer be any more instances of 'r' we delete it from our frequency_map, this breaks us from the while-loop bc now the frequency array is {a:2, c:1}

And the very last step is to constantly record the max_length - even when there are no duplicates to account for, we need to update the max_length, once we hit a duplicate we can calculate the window_size by doing (window_end-window_start+1)

So need to realize that:

(1): the frequency map controls our window_size - b/c once there are more than k distinct keys we trigger the while-loop
(2): While creating the frequency map, we're also expanding the window. Example:"araaci" -> when we add "araa" the max length is 4, once we reach the "c" we have encountered a new character and need to make adjustments to properly calculate the length of a subarray with k distinct arrays. Which is why we move the window_start pointer until we reach a character that no longer breaks the condition: len(char_frequency) > k:
(3): the while loop begins removing characters from left to right, causing the frequency map to reduce values for each key respectively, once we reach a character whose number of instances is 0 we can stop adjusting our window, because now there are only k distinct characters in it. We delete it from the map.

'''

def longest_substring_with_k_distinct(str1, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  for window_end in range(len(str1)):
    right_char = str1[window_end]

    # create a frequency map
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window

    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length

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

print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("araaci", 1))
print(longest_substring_with_k_distinct("cbbebi", 3))
