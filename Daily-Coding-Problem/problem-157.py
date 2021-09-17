def is_permutation_palindrome(s):
  # There are 128 ASCII characters
  arr = [0 for _ in range(128)]

  num_odds = 0
  for char in s:
    i = ord(char)
    arr[i] += 1

    if arr[i] % 2 != 0:
      num_odds += 1
    else:
      num_odds -= 1

  return num_odds <= 1
