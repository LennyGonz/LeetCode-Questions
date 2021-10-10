function smallest_subarray_with_given_sum(s, arr) {
  let window_start = 0;
  min_length = Infinity;
  window_sum = 0;

  for (window_end = 0; window_end < arr.length; window_end++) {
    window_sum += arr[window_end];

    while (window_sum >= s) {
      min_length = Math.min(min_length, window_end - window_start + 1);
      window_sum -= arr[window_start];
      window_start += 1;
    }
  }

  if (min_length == Infinity) {
    return 0;
  }

  return min_length;
}

console.log(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]));
