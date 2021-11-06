'''
Operators

Are used to perfrom arthimetic and logical operations on data
They enable us to manipulate and interpret data to produce useful outputs

Operators are represented by characters or special keywords

In general, python's operators follow the IN-FIX or PRE-FIX notations

In-fix operators appear between two operands (values on which the operator acts) and hence, are usually known as BINARY operators
Operand - operator - Operand -> Output

Pre-fix operator usually works on one operand and appears before it. Hence, prefi operators are known as UNARY operators
Operator operand -> Output

There are 5 main operator types in Python:

- arithmetic operators
- comparison operators
- assignment operators
- logical operators
- bitwise operators
'''

##############################
# Arithmetic Operators
##############################

'''
() - Parentheses    - Encapsulates the Precendent Operation
** - Exponent       - In-Fix
%  - Modulo         - In-Fix
*  - Multiplication - In-Fix
/  - Division       - In-Fix
// - Floor Division - In-Fix
+  - Addition       - In-Fix
-  - Subtraction    - In-Fix
'''
## Addition
print(10+5) # 15

float1 = 13.65
float2 = 3.40
print(float1 + float2) # 17.05

num = 20
flt = 10.5
print(num + flt) # 30.50

## Subtraction
print(10-5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)

## Multiplication
print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)


print(10.2 * 3)

## Division
print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)

print(12.4 / 2)

## Floor Division
print(43 // 10)

float1 = 5.5
float2 = 4.5
print(float1 // float2)

print(12.4 // 2)

## Modulo
print(10 % 2) # 0 -> No remainder if you divide 10 by 2

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10) # The remainder is positive if the right-hand operand is positive
print(28 % -10) # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5) # The remainder can be a float

## Precedence -> an arithmetic expression containing different operators will be computed on the basis of operator precedence
print(10-3*2) # multiplication first then subtration

print(3 * 20 / 5) # multiplication computed first, followed by division
print(3 / 20 * 5) # division computed first then multiplication

## Parentheses -> an expression which is enclosed inside parenthesis will be computed first, regardless of operator precedence
print((10-3)*2)
print((18+2)/(10%8))

###########################################################################################################################################################################
############################################################################ Comparison Operators #########################################################################
###########################################################################################################################################################################

'''
>        -> greater than
<        -> less than
>=       -> greater than or equal to
<=       -> less than or equal to
==       -> equal to
!=       -> not equal to
is       -> EQUAL TO
is not   -> NOT EQUAL TO

The result of a comparison is always a bool
If the comparison is correct, the value of the bool will be True. Otherwise, its value will be False

The == and != opeartors compare the values of both operands
However, the identity operators "is" and "is not", check whether the two operands are the EXACT SAME OBJECT
'''

num1 = 5
num2 = 10
num3 = 10
print(num2 > num1)
print(num1 > num2)

print(num2 == num3)
print(num3 != num1)

print(3+10 == 5 + 5)
print(3 <= 2)

###########################################################################################################################################################################
############################################################################ Assignment Operators #########################################################################
###########################################################################################################################################################################

'''
=   -> Assign
+=  -> Add and Assign
-=  -> Subtract and Assign
*=  -> Multiply and Assign
/=  -> Divide and Assign
//= -> Divide, Floor, and Assign
**= -> Raise power and Assign
|=  -> OR and Assign
&=  -> AND and Assign
^=  -> XOR and Assign
>>= -> Right-Shift and Assign
<<= -> Left-Shift and Assign
'''

year = 2020
print(year)

year = 2021
print(year)

year += 1
print(year)

first = 20
second = first 
first = 35
print(first, second) # 35 20

num = 10
print(num) # 10

num += 5
print(num) # 15

num -= 5
print(num) # 10

num *= 2
print(num) # 20

num /= 2
print(num) # 10.0

num **=2
print(num) # 100.0

########################################################################################################################################################################
############################################################################ Logical Operators #########################################################################
########################################################################################################################################################################

'''
and  - AND
or   - OR
not  - NOT
'''

my_bool = True or False
print(my_bool)

my_bool = True and False
print(my_bool)

my_bool = False
print(my_bool)

## Bit Value -> combinations of 1s and 0s form the foundation of programming
## In bit terms -> True == 1 and False == 0

print(10 * True)
print(10 * False)

# Python can automatically convert the bool to its numerical form when needed


########################################################################################################################################################################
############################################################################ Bitwise Operators #########################################################################
########################################################################################################################################################################

'''
&   - Bitwise AND
|   - Bitwise OR
^   - Bitwise XOR
~   - Bitwise NOT
<<  - Shift Bits Left
>>  - Shifts Bits Right
'''

num1 = 10 # binary value -> 01010
num2 - 20 # binary value -> 10100

print(num1 & num2)


num3 = 10
num4 = 10
print(num3 & num4)

'''
Bitwise AND

This operation takes a bit from num1 and the corresponding bit from num2 and performs an AND between them

In simple terms -> AND can be thought of as a multiplication between the 2 operands

num1 -> 01010 (10)
num2 -> 10100 (20)

At the first step, the first binary digits of both numbers are taken:

0 |1010
1 |0100

0 & 1 -> would give 0 (think of it as multiplication 1 * 0 = 0 OR 1(True) AND 0(False) = False)

Then we take the 2nd digits:
0| 1 | 010
1| 0 | 100
-> 0 AND 1 = 0(False)

01| 0 |10
10| 1 |00
-> 0 AND 1 = 0(False)

010| 1 |0
101| 0 |0
-> 1 AND 0 = 0(False)

that gives us 0000 -> 0
so 10 AND 20 = 0
'''

print(num1 | num2)
'''
Bitwise OR

It works similar to AND, but instead of multiplication it's addition
You can also apply the OR logic
1 or 1 == True or True -> True
1 or 0 == True or False -> True
0 or 1 == False or True -> True
0 or 0 == False or False -> False
'''


'''
Bitwise XOR(^) and NOT(~)
XOR and NOT will work on each bit as well

'''
print(num1 ^ num2)
print(~num1)

print(num1 << 3)
print(num2 >> 3)
'''
Bitwise Shift

The bitshift operations (>> and <<) simply move the bits to either the right or the left
When a binary number is shifted, a 0 also enters at the opposite end to keep the number of the same size

Let's supposed we have a binary number 0110(6) -> The operation we perform is 0110 >> 2:
0110 >> 2 
0011 (move one step to the right)
0001 (move one more step to the right)
Operation complete

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0110 << 2
01100 (move one step to the left)
011000 (move one more step to the left)
Operation complete

IN PYTHON -> leading zeroes are truncated
For example: the number 0011 will be the same as 11
Similarly, the number 00010111 will be the same as 1011
'''

###########################################################################################################################################################################
############################################################################ Comparison Operators #########################################################################
###########################################################################################################################################################################

'''
Strings are compatible with the comparison operators - each character has a unicode value
This allows strings to be compared on the basis of their unicode values

When 2 strings have different lengths, the string which comes first in the dictionary is said to have the smaller value
'''

print('a' < 'b') # 'a' has a smaller unicode value

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slyterin"

print(house == new_house)

print(new_house <= house)

print(new_house >= house)

first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name)

print("ha" * 3) # hahaha

random_string = "This is a random string"
print('of' in random_string) # Check whether 'of' exists in randomString

print('random' in random_string) # Check whether 'random' exists
