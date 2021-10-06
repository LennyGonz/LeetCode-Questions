/*
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

With the sliding window we need to be aware of our window
so we start with: window_start -> this helps me keep track of the beginning of the window & the first element of the window (we adjust this when we need to)

a mini objective is finding the condition for when we stop adding elements together and adjust the window
So we SHOULD focus on the indices of the array, and we can do that by using range(len(arr))

So the variable can be window_end, it'll continuously move until we reach the end of the array

Therefore, we can do window_end >= k-1 *remember arrays have 0-based indices so we account for this offset by doing "-1"
but this condition basically means, once the window_end hits the given size of the window (1) stop record the max_sum (2) adjust the window_sum by subtracting the first element in the window (3) adjust the beginning of the window and slide it to the right by 1 (4) restart everything

Keep this going until we reach the end of the array
*/

function max_sub_array_of_size_k(k, arr) {
  let window_start = 0;
  let max_sum = 0;
  let window_sum = 0;

  for (let window_end = 0; window_end < arr.length; window_end++) {
    window_sum += arr[window_end];

    if (window_end >= k - 1) {
      max_sum = Math.max(max_sum, window_sum);
      window_sum -= arr[window_start];
      window_start += 1;
    }
  }
  return max_sum;
}

console.log(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]));
