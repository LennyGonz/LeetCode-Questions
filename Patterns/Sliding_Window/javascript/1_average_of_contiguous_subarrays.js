/*
Given an array, find the average of all contiguous subarrays of size ‘K’ in it

ex: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

1. For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2(1+3+2+6−1)/5=>2.2
2. The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8(3+2+6−1+4)/5=>2.8
3. For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4(2+6−1+4+1)/5=>2.4
4. The next 5 numbers (subarray from index 3-7), the average is: (6-1+4+1+8)/5 => 3.6
5. Finally, the last 5 numbers (subarray from index 4-8), the average is: (-1+4+1+8+2)/5 => 2.8

Output: [2.2, 2.8, 2.4, 3.6, 2.8]

So if you look at the shift in subarrays there are always 4 elements that are overlapping in each iteration:

1st subarray: [1,3,2,6,-1]
2nd subarray: [3,2,6,-1,4]

We can REUSE the sum we calculated for the overlapping elements, by subtracting the first element of the window and adding the subsequent

We can continuously add the elements UNTIL our window size matches the given k
** remember arrays have a 0-based index so to account for that we do (k-1) **
Once our window size matches K, we take the average of the elements in the subarray and push it to our result list
Then we subtract the first element of our subarray (once we exit the if-statement the for-loop restarts and adds the next element)
Finally we adjust our window by moving up or sliding to the right. We can do this by adding 1 to window_start

But the critical condition that makes this work is: window_end >= K - 1
B/C we hit this condition, our window is the required size and we correctly calculate the average of the contiguous subarray
*/

function find_averages_of_subarrays(K, arr) {
  const result = [];
  let window_sum = 0;
  let window_start = 0;

  for (let window_end = 0; window_end < arr.length; window_end++) {
    window_sum += arr[window_end];

    if (window_end >= K - 1) {
      result.push(window_sum / K);
      window_sum -= arr[window_start];
      window_start += 1;
    }
  }

  return result;
}

const result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]);
console.log(`Averages of subarrays of size K: ${result}`);
