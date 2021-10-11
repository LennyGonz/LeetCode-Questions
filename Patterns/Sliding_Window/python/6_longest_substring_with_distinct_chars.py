'''
Given a string, find the length of the longest substring, which has all distinct characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".

So we can approach this problem similar Longest Substring with K distinct - however in that question we had more information specifically the "k"
The "k" would tell us how to size our window

In this problem we are NOT given that extra information... so we have to be aware of when to adjust our window

Since we need to resize our window the moment we encounter a repeated character - we know this is the condition we focus around

So to get started we can write an algorithm that will track an entire unqiue string,

We also need to remember we're returning a integer, we're approaching this problem with the sliding window technique so those are 2 variables to have

(1) max_length
(2) window_start

Now its also key to identify that when we reach a duplicate character, we shrink our window to the LAST occurance of that character so our substring only contains distinct characters

THE ONLY WAY - we can shrink our window is by keeping track of the indicies of each character
We can no longer move our window_start pointer 1 spot up when we hit a duplicate - we need it to jump 1 spot after its last occurance... why one spot after?

Well think about it: If we have "abba"

We iterate through the string -> "ab" -> update max_length to 2 -> window_start is still 0 no need to update

But then we hit a dupliate "b", if we move our window_start pointer to the first occurance -> window_start = 1
And then when we want to calculate the new length ... well window_end is 2 -> window_end-window_start+1 -> 2-1+1 = 2
But our window is looking like this: "bb" ... this is not a substring with distinct characters... so we have to add 1
window_start = char_index_map[right_char] + 1

That way when window_end = 2 (when we're at the second b) our pointers look like this

a b b a
    ^
    window_start
    window_end
    -> in the current window, we will not have any 'right_char' after its previous index
    -> this exposes another problem tho, when we reach the last iteration -> it takes us to character "a"
    the last instance of 'a' was at index 0 - the beginning of our window (window_start) is at index 2,
    if we update it to the last instance of a (0) + 1 ... window_start is 1 - and when we calculate max_length -> 3-1+1 = 3 but our substring looks like "ba" so clearly we need to factor this edge case...

    -> if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
    -> In other words -> window_start = max(window_start, char_index_map[right_char] + 1)
    -> Instead of sending our window_start pointer backwards, we keep it where it is

We can use a HashMap to remember the last index of each character we have processed
'''

def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  for window_end in range(len(str1)):
    # identify the character we're working with each respective iteration
    right_char = str1[window_end]

    # if the map already contains the 'right_char', shrink the window from the beginning so that we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      # 
      window_start = max(window_start, char_index_map[right_char] + 1)
    
    # insert the 'right_char' into the map - this is creating the index map
    char_index_map[right_char] = window_end

    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
	
  return max_length

print(non_repeat_substring("abba"))

'''
input: abba

window_start = 0
max_length = 0
char_index_map = {}


for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[0] -> right_char = "a"

  if "a" in char_index_map -> False
  if right_char in char_index_map:
    window_start = max(window_start, char_index_map[right_char] + 1)
  
  char_index_map['a'] = 0
  char_index_map[right_char] = window_end

  max_length = max(0, 0-0+1) = 1
  max_length = max(max_length, window_end - window_start + 1)

return max_length

2nd iteration
input: abba

window_start = 0
max_length = 1
char_index_map = {a:0}


for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[1] -> right_char = "b"

  if "b" in char_index_map -> False
  if right_char in char_index_map:
    window_start = max(window_start, char_index_map[right_char] + 1)
  
  char_index_map['b'] = 1
  char_index_map[right_char] = window_end

  max_length = max(0, 1-0+1) = 2
  max_length = max(max_length, window_end - window_start + 1)

return max_length

3rd iteration
input: abba

window_start = 0
max_length = 2
char_index_map = {a:0, b:1}


for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[2] -> right_char = "b"

  if "b" in char_index_map -> True
  if right_char in char_index_map:
    window_start = char_index_map['b'] + 1 = 1 + 1 = 2
    window_start = max(window_start, char_index_map[right_char] + 1)
  
  char_index_map['b'] = 1
  char_index_map[right_char] = window_end

  max_length = max(2, 2-2+1) = 2
  max_length = max(max_length, window_end - window_start + 1)

return max_length

4th iteration
input: abba

window_start = 2
max_length = 2
char_index_map = {a:0}


for window_end in range(len(str1)):
  right_char = str1[window_end] -> right_char = str1[3] -> right_char = "a"

  if "a" in char_index_map -> True
  if right_char in char_index_map:
    window_start = char_index_map[right_char] + 1 -> char_index_map['a']+1) -> 0 + 1 = 1 ** HERE IS THE PROBLEM
  
  char_index_map['a'] = 3
  char_index_map[right_char] = window_end

  max_length = max(2, 3-1+1) = 3 
  max_length = max(max_length, window_end - window_start + 1)

return max_length
'''
