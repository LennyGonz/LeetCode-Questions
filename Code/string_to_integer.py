def myAtoi(s):
  string = list(s.strip())
  if len(string) == 0:
    return 0
  
  sign = -1 if string[0] == '-' else 1

  if string[0] in ['-', '+']: del string[0]

  result = 0
  index = 0

  while index < len(string) and string[index].isdigit():
    result = result * 10 + ord(string[index]) - ord('0')
    
    index += 1
  
  return max(-2 ** 31, min(sign * result, 2 ** 31 - 1))
  
example1 = "42"
print("example1:",example1,"converted to string -->", myAtoi(example1))

example2 = "              -23"
print("example2:", example2, "converted to string -->", myAtoi(example2))

example3 = "0099"
print("example3:", example3, "converted to string -->", myAtoi(example3))
