'''
Functions are useful because they make the code concise and simple - primary benefits of using functions are

Reusability: A function can be used over and over again. You do not have to write redundant code
Simplicity: Functions are easy to use and make the code readable. We only need to know the inputs and the purpose of the function without fousing on the inner workings

There are 2 types of functions:

1) Built-in functions
2) User-defined functions

template of a function: keyword: "def" & function Name & parameters

def functionName(parameters)

functionName - is just the name we use to identify the function
parameters - of a function are the inpus for that function. We can use the inputs within the function
The body of the function constains the set of operations that the function will perform
'''

def printFunction():
  print("this is a function")

'''
Function Parameters

They are the means of passing data to the function. This data can be used by the function to perform a meaningful task

The actual value/variables passed into the parameters are known as ARGUMENTS
'''
def minimum(first, second):
  if(first < second):
    print(first)
  else:
    print(second)

num1 = 10
num2 = 20
minimum(num1, num2)

'''
Return Statement

To return something from a function, we must use the RETURN keyword

Once the return keyword is executed, the compiler ends the function. Any remaining lines of code after the return statement will not be executed
'''
def maximum(first, second):
  if(first < second):
    return first
  return second

num3 = 40
num4 = 50
result = maximum(num3, num4)
print(result)

'''
Function Scope

The scope of a function means the extent to which the variables and the other data items made inside the function are accessible in code

In python, the function scope IS the functions body

Data Lifecycle !!!!!!!!!

In Python, data created inside the function cannot be used from the outside UNLESS it is being returned from the function

Variables in a function are isolated from the rest of the program. When the function ends, they are released from memory and cannot be recovered

The following code will NEVER work:
'''

def func():
  name = "Stark"

func()
#print(name) # Accessing 'name' outside the function

'''
As we can see, the name variable doesn't exist in the outer scope, and Python throws an error

Similarly, the function cannot access data OUTSIDE the scope unless the data has been passed in as an argument
'''

'''
ALTERING DATA

When mutable data is passed to a function, the function can modify it or alter it

These modifications will stay in effect outside the function scope as well.

An example of mutable data is a LIST!

In the case of IMMUTABLE data, the function can modify it, but the data will remain unchanged outside the function's scope
Examples of immutable data are:

- numbers
- strings etc
'''

num = 20 
def mulitplyBy2(n):
  n *= 10
  num = n
  print("value of num inside of function:", num) # num = 200
  return n

mulitplyBy2(num)
print("value of num outside function:", num) # num = 20

'''
So now it is confirmed that immutable objects are unaffected by the working of a function
If we really need to update immutable variables through a function, we can simply assign the returning value from the function to the variable

Now we'll try updating a mutable object through a function
'''

num_list = [10,20,30,40]
print("num_list before the function",num_list)

def multiplyBy10(my_list):
  for n in range(len(my_list)):
    my_list[n] *= 10

multiplyBy10(num_list)

print("num_list after the function",num_list)

'''
we passed num_list to our function as the my_list parameter
Now any changes made to my_list will reflect in num_list outside the function
This would NOT happen in the case of an immutable variable
'''

'''
Built-In Functions

Strings have their own built in functions
Type Conversions

Functions that are properties of a articular entity are known as METHODS
These methods can be accessed using the "." operator (dot operator)
String data type has several methods associated with it

Search!
An alternative for finding a substring using the "in" keyword is the "find()" method
It returns the first index at which a substring occurs in a string. If NO instance of the substring is found, the method returns -1

-1 is a conventional value that represents a None or failure in case the output was supposed to be positive

For a string called a_string, find() can be used in the following way
'''
a_string = "Lenny"

# a_string.find(substring, start, end)

# substring - is what we're searching for
# start - is the index from which we start searching in a_string
# end - is the index where we stop our search in a_string
# START and END are OPTIONAL
print(a_string.find("en"))
print(a_string.find("y"))

'''
Replace() - method can be used to replace a part of a substring with another string
b_string.replace(substring_to_be_replace, new_string)
'''
b_string = "Welcome To New York"
new_string = b_string.replace("Welcome To", "Greetings from")
print(b_string)
print(new_string)

# We can also change the letter case -> using upper() and lower()
print("uppercase".upper())
print("LOWERCASE".lower())

'''
Type Conversions

int() -> ONLY A STRING can be converted to an integer

ord() -> converts a character to its unicode value

float() -> translates data into a floating point number

str() -> converts data into a string

bool() -> takes in data and gives us the correspinding boolean value | Strings are always True except empty strings | Floats and integers with a value of 0 are False
'''
# string to INT
print(int("12")*10)

# ord()
print(ord("a"))

# float()
print(float(24))

# str()
print(str(12))

# bool()
print(bool(10))

#######################################################################################################################################################################
################################################################# Lambda ##############################################################################################
#######################################################################################################################################################################

'''
A Lambda Function is an ANONYMOUS FNUCTION that returns some form of data

Lambdas are defined using the lambda keyword, since they return data, it is a good practice to assign them to a variable

Syntax:

lamba paramters : expression

If you have multiple parameters separate them using commas
Expression -> An operation that returns something
'''
triple = lambda num : num * 3 # assigning the lambda to a variable
print(triple(10)) # 30  -> calling the lambda and giving it a parameter

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web")) # -> "WWW" 

'''
As we can see lambdas are simpler and more readable than normal functions
BUT this simplicity comes with a limitation

A lambda cannot have a multi-line expression -> this means that our expression needs to be something that can be written in a single line

We can also use conditionals with lambdas
'''

my_func = lambda num : "High" if num > 50 else "low"

print(my_func(100))
print(my_func(10))

'''
When using conditional statements in lambdas, the if-else pair IS NECESSARY
Both cases NEED to be covered, otherwise, the lambda will throw an error

The purpose of lambda is when a function requires another function as its argument


Functions As Arguments

In Python, one function can become an argument for another function. This is useful in many cases

Let's make a calculator function that requires the:
- add
- subtract
- multiply
- divide

function along with 2 numbers as arguments
'''
def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


def calculator(operation, n1, n2):
  return operation(n1, n2)  # Using the 'operation' argument as a function


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

# Python understands that the multiply arugment is a function, and so, everything works perfectly

'''
Using Lambdas

Now is Lambda's time to shine, we needed to write four extra functions that could be used as the argument ... this can be a hassle
Why dont we just pas a lambda as an argument?
'''
def calculator(operation, n1, n2):
  return operation(n1, n2)  # Using the 'operation' argument as a function


# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))

'''
Now we can define the operation on the go...

The built-in map() function creates a map object using an existing list and a function as its parameters.
This object can be converted to a list using the list() function (more on this later).

The template for map() is as follows: map(function, list)
'''

num_list9 = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list9)

print(list(double_list))

'''
This creates a new list. The original list remains unchanged.

We could have created a function that doubles a number and used it as the argument in map(), but the lambda made things simpler.

Another similar example is the filter() function. It requires a function and a list.

filter() filters elements from a list if the elements satisfy the condition that is specified in the argument function.

Let’s write a filter() function that filters all the elements which are greater than 10:
'''
numList4 = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList4))
print(greater_than_10)

'''
The function returns a filter object which can be converted to a list using list().

just like map(), filter() returns a new object without changing the original list.
'''

#######################################################################################################################################################################
################################################################# Recursion ###########################################################################################
#######################################################################################################################################################################

'''
Recursion is the process in which a function calls itself during its execution. 
Each recursive call takes the program one scope deeper into the function.

The recursive calls stop at the base case. The base case is a check used to indicate that there should be no further recursion.

Here's a simple example:
'''
def rec_count(number):
  print(number)
  # Base case
  if number == 0:
    return 0
  rec_count(number - 1)  # A recursive call with a different argument
  print(number)


rec_count(5) # 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> 1 -> 2 -> 3 -> 4 -> 5

'''
This is fairly easy to understand. In each call, the value of the number variable is printed. 
We then check whether the base case has been fulfilled. If not, we make a recursive call to the function with the current value decremented.

One thing to notice is that an outer call cannot move forward until all the inner recursive calls have finished. This is why we get a sequence of 5 to 0 to 5.

Why Use Recursion?

Recursion is a concept which many find difficult to grasp at first, but it has its advantages.
For starters, it can significantly reduce the runtime of certain algorithms, which makes the code more efficient.

Recursion also allows us to easily solve many problems related to graphs and trees, things you may study in the future. It is also important in search algorithms.

However, we need to be careful when using recursion.

If we don’t specify an appropriate base case or update our arguments as we recurse, the program will reach infinite recursion and crash.

The arguments passed to our recursive function are updated in each recursive call so that the base case can eventually be reached.
'''

def fib(n):
  # The base cases
  if n <= 1:  # First number in the sequence
    return 0
  elif n == 2:  # Second number in the sequence
    return 1
  else:
    # Recursive call
    return fib(n - 1) + fib(n - 2)


print(fib(6))

'''
First, we handle our base cases. We know that the first two values are always 0 and 1, so that is where we can stop our recursive calls.

If n is larger than 2, then it will be the sum of the two values before it.
'''

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1

  if n < 0:
    return -1
  # Recursive call
  return n * factorial(n - 1)


print(factorial(5))
