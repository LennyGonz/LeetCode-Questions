/*
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

*/

function longest_substring_with_k_distinct(str1, k) {
  let charFrequency = {};
  maxLength = 0;
  windowStart = 0;

  for (windowEnd = 0; windowEnd < str1.length; windowEnd++) {
    rightChar = str1[windowEnd];

    if (!(rightChar in charFrequency)) {
      charFrequency[rightChar] = 0;
    }
    charFrequency[rightChar] += 1;

    while (Object.keys(charFrequency).length > k) {
      let leftChar = str1[windowStart];
      charFrequency[leftChar] -= 1;
      if (charFrequency[leftChar] === 0) {
        delete charFrequency[leftChar];
      }
      windowStart += 1;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }

  return maxLength;
}

console.log(
  `Length of the longest substring: ${longest_substring_with_k_distinct(
    "araaci",
    2
  )}`
);
console.log(
  `Length of the longest substring: ${longest_substring_with_k_distinct(
    "araaci",
    1
  )}`
);
console.log(
  `Length of the longest substring: ${longest_substring_with_k_distinct(
    "cbbebi",
    3
  )}`
);

/**
 * Time: O(n)
 * Space: O(1)
 */

/**
 * ask clarifying questions - edge cases, see how the algoirthm run in that case
 * alphanumeric, ascii, unicode - shows youre aware of all scenarios (all edge cases)
 * confirm you have 2 substrings that are equally long
 *
 * describe your algorithm
 * go thru an example with the alogirthm you have in mind
 *
 * Introduce trade-offs if you switch data structures, or just mention it when youre talking
 *
 * Start off with a method declaration
 * def longest_substring_with_k_distinct(k, str):
 *  return intt
 *
 * BE SPECIFIC IN THE BEHAVORIAL - GIVE EXAMPLES
 */
