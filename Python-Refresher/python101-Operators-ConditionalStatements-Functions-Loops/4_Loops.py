'''
A loop is a control structure that is used to perform a set of instructions for a specific number of times.

Loops solve the problem of having to write the same set of instructions over and over again. We can specify the number of times we want the code to execute.

One of the biggest applications of loops is traversing data structures, e.g. lists, tuples, sets, etc. 
In such a case, the loop iterates over the elements of the data structure while performing a set of operations each time.
Don’t worry about them for now. We’ll explore them in the next section.

Just like conditional statements, a loop is classified as a control structure because it directs the flow of a program by making varying decisions in its iterations. 

There are two types of loops that we can use in Python:

- The "for" loop
- The "while" loop

A for loop uses an iterator to traverse a sequence, e.g. a range of numbers, the elements of a list, etc.
In simple terms, the iterator is a variable that goes through the list.

The iterator starts from the beginning of the sequence. In each iteration, the iterator updates to the next value in the sequence.

The loop ends when the iterator reaches the end.

In a for loop, we need to define three main things:

1) The name of the iterator
2) The sequence to be traversed
3) The set of operations to perform

The loop always begins with the for keyword. The body of the loop is indented to the right

for iterator in Sequence

The "in" keyword specifies that the iterator will go through the values in the sequence/data structure.

In Python, the built-in range() function can be used to create a sequence of integers.

This sequence can be iterated over through a loop. A range is specified in the following format:

range(start, end, step)

The end value is not included in the list.

If the start index is not specified, its default value is 0.

The step decides the number of steps the iterator jumps ahead after each iteration.
It is optional and if we don’t specify it, the default step is 1, which means that the iterator will move forward by one step after each iteration.

Let’s take a look at how a for loop iterates through a range of integers:
'''

for i in range(1, 11):  # A sequence from 1 to 10
  if i % 2 == 0:
    print(i, " is even")
  else:
    print(i, " is odd")

'''
As we can see above, rather than individually checking whether every integer from 1 to 10 is even or odd, we can loop through the sequence and compute i % 2 == 0 for each element.

The iterator, i, begins from 1 and becomes every succeeding value in the sequence.

Let’s see how a loop changes when the step component of a range is specified:
'''

for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
  print(i)

# Looping Through a List/String 

'''
A list or string can be iterated through its indices.

Let’s double each value in a list using a for loop:
'''

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
  float_list[i] = float_list[i] * 2

print(float_list)

# We could also traverse the elements of a list/string directly through the iterator. In the float_list above, let’s check how many elements are greater than 10:
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list:  # Iterator traverses to the last index of the list
  if num > 10:
    count_greater += 1

print(count_greater)
# In this example, num is the iterator. 
# An important thing to keep in mind is that in the case above, altering num will not alter the actual value in the list.
# The iterator makes a copy of the list element.

########################################################################################################################################
'''
Execution of Nested Loops

Python lets us easily create loops within loops. There’s only one catch: the inner loop will always complete before the outer loop.

For each iteration of the outer loop, the iterator in the inner loop will complete its iterations for the given range, after which the outer loop can move to the next iteration
'''
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
  for n2 in num_list:  # Now we have two iterators
    if(n1 + n2 == n):
      print(n1, n2)

# In the code above, each element is compared with every other element to check if n1 + n2 is equal to n. This is the power of nested loops!

'''
Break Keyword

Sometimes, we need to exit the loop before it reaches the end. This can happen if we have found what we were looking for and don’t need to make any more computations in the loop.

A perfect example is the one we have just covered. At a certain point, n1 is 23 and n2 is 27. Our condition of n1 + n2 == n has been fulfilled. But the loops keep running and comparing all other pairs as well. This is why the pair is printed twice. It would be nice to just stop it when the pair is found once.

That’s what the break keyword is for. It can break the loop whenever we want.

Let’s add it to the example above:
'''
n_ = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
  for n2 in num_list:
    if(n1 + n2 == n_):
      found = True  # Set found to True
      break  # Break inner loop if a pair is found
  if found:
    print(n1, n2) # Print the pair
    break  # Break outer loop if a pair is found

'''
As we can see, only (23, 27) is printed this time.

This is because (23, 27) is the first pair which satisfies the condition. We terminate the loop after that using the found bool. Hence, (27, 23) is never computed.
'''

'''
Continue Keyword

When the continue keyword is used, the rest of that particular iteration is skipped. 

The loop continues on to the next iteration. We can say that it doesn’t break the loop, but it skips all the code in the current iteration and moves to the next one.

We don’t need to get into too much detail, so here’s a simple example:
'''
num_list4 = list(range(0, 10))

for num in num_list4:
  if num == 3 or num == 6 or num == 8:
    continue
  print(num)

'''
The loop goes into the if block when num is 3, 6, or 8. 
When this happens, continue is executed and the rest of the iteration, including the print() statement, is skipped.
'''

'''
Pass Keyword

In all practical meaning, the pass statement does nothing to the code execution. It can be used to represent an area of code that needs to be written. Hence, it is simply there to assist you when you haven’t written a piece of code but still need your entire program to execute.

num_list = list(range(20))

for num in num_list:
  pass # You can write code here later on

print(len(num_list)) 
'''

#######################################################################################################################################################################

'''
The while loop keeps iterating over a certain set of operations as long as a certain condition holds True.

It operates using the following logic:

While this condition is true, keep the loop running.
'''

ex = 2  # Could be any number
power = 0
val = ex
while val < 1000:
  power += 1
  val *= ex
print(power) # 9

# In each iteration, we update val and check if its value is less than 1000.
# The value of power tells us the maximum power n can have before it becomes greater than or equal to 1000. Think of it as a counter.

'''
We can also use while loops with data structures, especially in cases where the length of data structure changes during iterations.

The following loop computes the sum of the first and the last digits of any integer:
'''
n = 249
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
  first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print(result)

'''
Cautionary Measures

Compared to for loops, we should be more careful when creating while loops. This is because a while loop has the potential to never end. This could crash a program!

Have a look at these simple loops:

while(True):
  print("Hello World")

x = 1
while(x > 0):
  x += 5
  
The loops above will never end because their conditions always remain true.
Hence, we should always make sure that our condition has a mutable variable/object that is being updated in the loop and will eventually turn the condition false.

The break, continue, and pass keywords work with while loops.

Like for loops, we can also nest while loops. Furthermore, we can nest the two types of loops with each other.

#######################################################################################################################################################################

Iteration vs. Recursion 

If we observe closely, there are several similarities between iteration and recursion. 

In recursion, a function performs the same set of operations repeatedly but with different arguments.

A loop does the same thing except that the value of the iterator and other variables in the loop’s body change in each iteration.

Figuring out which approach to use is an intuitive process. Many problems can be solved through both.

Recursion is useful when we need to divide data into different chunks. 

Iteration is useful for traversing data and also when we don’t want the program’s scope to change.
'''

# PRACTICE PROBLEMS

'''
Given a string containing only square brackets, [], you must check whether the brackets are balanced or not. The brackets are said to be balanced if, for every opening bracket, there is a closing bracket.

You will write your code in the check_balance() function, which returns True if the brackets are balanced and False if they are not.

For an empty string, the function will return True.
'''
def check_balance(brackets):
  def balanced(brackets, startIndex = 0, currentIndex = 0):
    if currentIndex == len(brackets):
      return startIndex == 0

    if startIndex < 0:
      return False
    
    if brackets[currentIndex] == "[":
      return balanced(brackets, startIndex+1, currentIndex+1)
    
    if brackets[currentIndex] == "]":
      return balanced(brackets, startIndex-1, currentIndex+1)
  
  return balanced(brackets)

example1 = "[[[]]][]"
print(check_balance(example1))

def check_balance_iterative(brackets):
  check = 0
  for bracket in brackets:
    if bracket == '[':
      check += 1

    elif bracket == ']':
      check -= 1

    if check < 0:
      break

  return check == 0

print(check_balance_iterative(example1))
