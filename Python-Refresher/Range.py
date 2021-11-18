'''
Range type represents an immutable sequence of numbers and
is used for LOOPING a specific number of time in FOR loop

Syntax ==> range(stop)
Syntax ==> range(start, stop[,step])

The arguments to the range constructor MUST BE integers
When using range() and you don't include 'start' it
defaults to 0.

list(range(10))
[0,1,2,3,4,5,6,7,8,9]

Notice we omitted the start parameter, therefore it defaults
at 0 and it ends at 10 numbers later

list(range(1,11))
[1,2,3,4,5,6,7,8,9,10]

Notice it's inclusive of start, but exclusive of end
[start, n-1]
[1, 11-1] --> [1, 10]

list(range(0,30,5))
[0,5,10,15,20,25]

Inclusive of start and exclusive of stop
Print numbers 0-29 that are intervals of 5

That's why we start at 0 and end at 25
'''

print("This prints list(range(10)): ",list(range(10)))

print(" ")

print("This prints list(range(1,11)): ", list(range(1,11)))

print(" ")

print("This prints list(range(0,30,5)): ",list(range(0,30,5)))

print("")

matrix = [[2,3,4,5],
          [5,3,6,7],
          [9,3,7,1],
          [1,2,3,4]]

width = len(matrix[0])
print("Width is",width)

print("")

for i in range(len(matrix)):
    # iterate from 0-3
    print(i)