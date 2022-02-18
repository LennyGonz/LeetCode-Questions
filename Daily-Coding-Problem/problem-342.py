'''
Let's work backwards from the function definition to implement it.

We're given a list, a function that takes in a value from the list and an accumulator, and an initial value.

From what we're given, we can initialize our accumulator to be the initial value, and iterate over the list, calling f on the current element with the accumulator, and then finally return the accumulator:
'''
def reduce(lst, f, initial):
  acc = initial
  for e in lst:
    acc = f(e, acc)
  return acc

'''
To show how this works, let's go back to the sum example.

Recall that f in this example adds up two numbers a and b, and that we call reduce with an initial value of 0.

Then, if we could unroll the function, it would look like this:

add(5, add(4, add(3, add(2, add(1, 0)))))

Where add is defined as a + b.

This function takes O(N * f) time, since we iterate over the list and call f on each element given to us.
'''
