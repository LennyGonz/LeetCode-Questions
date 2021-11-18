# A Conditional Statement is a Boolean expression that, if True, executes a piece of code

# It allows programs to branch out into different paths based on Boolean expressions result in True or False outcomes

# Conditional Statements control the flow of the code and allow the computer to think - Hence they are classified as control structures

'''
if conditional statement is True:
  # execute expression1
  pass
else:
  # execute expression2
  pass

There are three types of conditional statements in python:
- if
- if-else
- if-elif-else

The flow of an if-statement

IF the CONDITION holds true, execute the code to be executed.
OTHERWISE, skip it and move on
'''

num = 5

if (num == 5):
  print("The number is equal to 5")
if num > 5:
  print("The number is greater than 5")

# Conditions with Logical Operators
num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
  print("The number is a multiple of 2, 3, and 4")

if (num % 5 == 0 or num % 6 == 0):
  print("The number is a multiple of 5 and/or 6")

num = 63

if num >= 0 and num <= 100:
  if num >= 50 and num <= 75:
    if num >= 60 and num <= 70:
      print("The number is in the 60-70 range")

num = 10

if num > 5:
  num = 20
  new_num = num * 5

# The if condition ends, but the changes made inside it remain
print(num)
print(new_num)

'''
if condition is True:
  execute this code block
else:
  execute this code block instead
'''

num = 60

if num <= 50:
  print("The number is less than or equal to 50")
else:
  print("The number is greater than 50")

# We can also have 2-ifs
num = 70
if num <= 50:
  print("The number is less than or equal to 50")
if num > 50:
  print("The number is greater than 50")

## Conditional Expressions
'''
Conditional expressions use the functionality of an if-else statement in a different way

The expression returns an OUTPUT based on the condition we provide -> this output can be stored in a variable

A conditional expression can be written in the following way:

output_value1 if condition else output_value2

If the if-condition is fulfilled, the output would be output_value1
Otherwise, it would be output_value2
'''

num = 90

# using backslash for line continuation
output = "The number is less than or equal to 50" \
  if num <= 50 else "The number is greater than 50"

print(output)

'''
if condition1:
  execute this code block, if conditon1 is true
elif condition2:
  execute this code block, if condition1 is false AND condition2 is true
else:
  execute this code block, if condition1 is FALSE AND condition2 is FALSE
'''

light = "Red"

if light == "Green":
  print("Go")
elif light == "Yellow":
  print("Caution")
elif light == "Red":
  print("Stop")
else:
  print("Incorrect light signal")

'''
if-elif-else or if-elif statements are NOT the same as multiple if-statements -> IF statements act independently
'''

num = 10
if num > 5:
  print("The number is greater than 5")
elif num % 2 == 0:
  print("The number is even")
else:
  print("The number is odd and less than or equal to 5")
# This will only print -> "The number is greater than 5"

num = 4
if num < 5:
  print("The number is less than 5")
if num % 2 == 0:
  print("The number is even")
if not num % 2 == 0:
  print("The number is odd")
# This will print -> "The number is less than 5" & "The number is even"
