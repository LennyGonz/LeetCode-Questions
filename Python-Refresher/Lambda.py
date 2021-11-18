'''
Lambda function (Anonymous Functions)

the lambda keyword is used to create anonymous functions

syntax: lambda arguments: expression

* This function can have any number of arguments but only
one expression, which is evaluated and returned

* One is free to use lambda functions wherever function 
objects are required

* You need to keep in your knowledge that lambda functions
are syntactically restricted to a single expression

def cube(y):
	return y*y*y

g = lambda x: x*x*x
print(g(7))

print(cube(7))


Filter() function
The filter function takes in A LIST and A FUNCTION as arguments. 
This way is meant to filter out all the elements 
of a sequence, for which the function returns True.

# filter() with lambda()
# filtering out even numbers
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(filter(lambda x: (x%2 != 0), li ))
print(final_list)
final_list = [5, 7, 97, 77, 23, 73, 61]

x%2 != 0 (wil return all odd)
x%2 = 0 (will return all even)

Map() function
The map() function takes in A FUNCTION and A LIST as arguments
Map() is called with a lambda function and a list and a 
new list is returned which contains all the lambda modified
items returned by that function for each item.

Basically we apply a function to each element in a list

map() with lambda()
to get double of a list
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x: x*2, li))

print(final_list)
final_list = [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

reduce()
The reduce() function takes in A FUNCTION and A LIST as arguments
reduce() is called with a lambda function and a list and a new reduced result is
returned. This performs a A REPETITIVE OPERATION over the PAIRS OF THE LIST

reduce() with lambda()
to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) --> sum = 193

5+8    = 13 
13+10  = 23
23+20  = 43
43+50  = 93
93+100 = 193
sum    = 193

(((((5+8)+10)+20)+50)+100)
'''



