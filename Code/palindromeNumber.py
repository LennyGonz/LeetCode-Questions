def is_Palindrome(num):
  number, reversed_number = num, 0

  while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = int(number / 10)
  
  return num == reversed_number

ex1 = 121
print(is_Palindrome(ex1))
