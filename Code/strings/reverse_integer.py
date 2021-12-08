def reverse(digit):

  if digit < 0:
    sign = -1
    digit = -digit
  else:
    sign = 1
  
  reversed_num = 0

  while digit:
    last_digit = digit % 10
    reversed_num = (reversed_num * 10) + last_digit
    digit = digit // 10
  
  return 0 if reversed_num > pow(2,31) else reversed_num * sign


example1 = 123
example2 = -789
print("Input:",example1, "==> revered is:", reverse(example1))
print("Input:", example2, "==> revered is:", reverse(example2))
