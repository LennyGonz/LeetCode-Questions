def check_palindrome(num):
  # Find the divisor needed to obtain the first digit.
  divisor = 1
  while (num / divisor >= 10):
    divisor *= 10

  while (num != 0):
    first = num / divisor
    last = num % 10

    if (first != last):
      return False

    num = (num % divisor) / 10

    # The number of digits has been reduced by 2, so our divisor is reduced by 10 ** 2.
    divisor = divisor / 100

  return True
