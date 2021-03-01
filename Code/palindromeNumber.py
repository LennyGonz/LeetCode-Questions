def is_Palindrome(number):
  num = number
  reversed_num = 0

  while num > 0:
    last_digit = num % 10
    reversed_num = (reversed_num * 10) + last_digit
    num = int(num / 10)
  
  return number == reversed_num

ex1 = 121
print(is_Palindrome(ex1))
