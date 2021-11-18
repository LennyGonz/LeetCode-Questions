'''
Python has 3 main data types:
- Numbers
- Strings
- Booleans

There are 3 main types of numbers in python:

- Integers
- Floating Point Numbers
- Complex Numbers
'''

print(10) # a positive integer
print(-3000) # a negative integer

num = 123456789 # assigning an integer to a variable
print(num)

num = -16000 # assigning a new integer
print(num)

print(1.0000000000000000005) # a positive float
print(-85.6701) # a negative float

flt_pt = 1.23456789
print(flt_pt)

# In python the imaginary part of a complex number is denoted by j - Python follows the electrical engineering convention
print(complex(10, 20)) # represents the complex number (10 + 20j)
print(complex(2.5,-18.2)) # represents the complex number (2.5 - 18.2j)


'''
Booleans (bool) data type allows us to choose between two values: True and False
'''

print(True)

f_bool = False
print(f_bool)

'''
A String is a collection of characters closed within single or double quotation marks
'''

print("Harry Potter!")

got = 'Game of Thrones....' # Single quotation Marks
print(got)
print("$")

empty = ""
print(empty) # prints an empty line

# The length of a string can be found using the len() built-in function
random_string = "I am Batman" #11 characters
print(len(random_string))

'''
Indexing

In a string, every character is given a numerical index based on its position

A string in python is indexed from 0 to n-1 where n is its length

This means that the index of the first character in a string is 0

| 0 | 1 | 2 | 3 | 4 |
| H | E | L | L | O |

Accessing Characters can be done through indexing -> we index using square brackets
'''
batman = "Bruce Wayne"

first = batman[0] # B
print(first)

space = batman[5] # Accessing the empty space in the string
print(space)

last = batman[len(batman)-1]
print(last)

'''
Reverse Indexing

We can also change our indexing convention by using negative indices

Negative indices start from the opposite end of the string. Hence, the -1 index corresponds to the last character:
'''
batman = "Bruce Wayne"
print(batman[-1]) # Corresponds to batman [10]
print(batman[-5]) # Corresponds to batman [6]

'''
String Slicing

Slicing is the proces of obtaining a portion (substring) of a string by using its indices

Given a string, we can use the following to slice it and obtain a substring: string[start:end]
- start: is the index from where we want the substring to start
- end: is the index where we want our substring to end

The character at the "end" index in the subtring, will NOT be included in the substring obtained through this method

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| T | H | I | S |   | I | S |   | M | Y |    | S  | T  | R  | I  | N  | G  |
'''
my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index => "This"
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end 

'''
Slicing with a step

We can define a step through which we can skip characters in the string.
The default step is 1, so we iterate through the string one character at a time

The step is defined after the end index -> string[start:end:step]
'''

my_string = "This is MY string!"

print(my_string[0:7]) # A step of 1 -> This is
print(my_string[0:7:2]) # A step of 2 -> Ti s
print(my_string[0:7:5]) # A step of 5 -> Ti

'''
Reverse Slicing

Strings can also be sliced to return a reversed substring
In this case we would switch the order of the "start" and "end" indices

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| T | H | I | S |   | I | S |   | M | Y |    | S  | T  | R  | I  | N  | G  |  ! |
'''
my_string = "This is MY string!"
print(my_string[13:2:-1]) # -> start at index 13 stop at index 2 -> rts YM si s
print(my_string[17:0:-2]) # -> start at index 17 stop at index 0 -> !nrsY ish

'''
Partial Slicing

One thing to note is specifying the start and end indices is optional

if start is NOT provided, the substring will have all the characters until the end index.
if end is NOT provided, the substring will begin from the start index and go all the way to the end
'''
my_string = "This is MY string!"
print(my_string[:8]) # all the characters before M
print(my_string[8:]) # all the characters starting from M
print(my_string[:]) # the whole string
print(my_string[:-1])
print(my_string[::-1]) # the whole string in reverse (step is -1)
