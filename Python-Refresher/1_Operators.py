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


