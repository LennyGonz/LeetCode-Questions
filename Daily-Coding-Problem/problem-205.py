def get_next_permutation(num):
  num, n = list(num), len(num)

  # Get the first digit of the "tail".
  tail_start = n - 1
  while tail_start >= 0 and num[tail_start - 1] > num[tail_start]:
    tail_start -= 1

  # If the entire list is sorted in descending order, there is no larger permutation.
  if tail_start == 0:
    return None

  # Find the smallest digit in the tail that is greater than the element we need to swap.
  swap = tail_start
  while swap < n and num[tail_start - 1] < num[swap]:
    swap += 1
  swap -= 1

  # Perform the swap.
  num[tail_start - 1], num[swap] = num[swap], num[tail_start - 1]

  # Reverse the tail elements.
  start, end = tail_start, len(num) - 1
  while start < end:
    num[start], num[end] = num[end], num[start]
    start += 1; end -= 1

  return num
