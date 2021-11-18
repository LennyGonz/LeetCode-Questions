# Data Structures in Python

## Lists

### append

append()...appends an object to the end of the list

```python
>>> stack = ['a','b']
>>> stack.append('c')
>>> stack
['a', 'b', 'c']
```

### pop

remove the last element of a list

```python
>>> my_list.pop()
'a'
>>> my_list
['b', 'c', 'b']
```

### extend

extend()...appends each element of the iterable object to the end of the list

```python
>>> stack.append(['d', 'e', 'f'])
>>> stack
['a', 'b', 'c', ['d', 'e', 'f']]
```

The object ['d', 'e', 'f'] has been appended to the exiistng list.
However, it happens that sometimes what we want is to append the elements one by one of a given list rather the list itself.
You can do that manually of course, but a better solution is to use the extend() method as follows:

```python
>>> stack = ['a', 'b', 'c']
>>> stack.extend(['d', 'e','f'])
>>> stack
['a', 'b', 'c', 'd', 'e', 'f']
```

### insert

You can remove element but also insert element wherever you want in a list:

```python
my_list.insert(2, 'a')
my_list
['b', 'c', 'a', 'b']
```

### slicing

Slicing uses the symbol `:`

```python
>>> list[first index:last index:step]
>>> list[:]

>>> a = [0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
>>> a[2:]
[2, 3, 4, 5]
>>> a[:2]
[0, 1]
>>> a[2:-1]
[2, 3, 4]
```

By default the first index is 0, the last index is the last one..., and the step is 1

```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8]
>>> a[:]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[::1]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[0::1]
[1, 2, 3, 4, 5, 6, 7, 8]
```

### List comprehension

Traditionally, a piece of code that loops over a sequence could be written as follows:

```python
>>> evens = []
>>> for i in range(10):
...     if i % 2 == 0:
...         evens.append(i)
>>> evens
[0, 2, 4, 6, 8]
```

This may work, but it makes things slower for python b/c the interpreter works on each loop to determine what part of the sequence has to be changed

A **list comprehension** is the correct answer:

```python
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
```

Besides the fact that it is more efficient, it is also shorter and involves fewer elements

Syntax: `[expression for item in list]`

```python
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
```

Output: `[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`

```python
letters = list(map(lambda x: x, 'human'))
print(letters)
```

Output: `['h', 'u', 'm', 'a', 'n']`

### Lists as Stacks

Remember stacks are LIFO (last-in, first-out)
An item can be added to a list by using `append()` method
The last item can be removed from the list by using the `pop()` method without passing any index to it

```python
>>> stack = ['a','b','c','d']
>>> stack.append('e')
>>> stack.append('f')
>>> stack
['a', 'b', 'c', 'd', 'e', 'f']
>>> stack.pop()
'f'
>>> stack
['a, 'b', 'c', 'd', 'e']
```

### Lists as Queues

Another usage of list is using it as a Queue -- first in, first out (FIFO)

```python
>>> queue = ['a', 'b', 'c', 'd']
>>> queue.append('e')
>>> queue.append('f')
>>> queue
['a', 'b', 'c', 'd', 'e', 'f']
>>> queue.pop(0)
'a'
```

## Tuples

Tuples are optimized, which makes them very simple objects.
There are two methods available only:

- *index:* to find the occurence of a value
- *conut:* to count the number of occurences of a value

```python
>>> l = (1,2,3,1)
>>> l.count(1)
2
>>> l.index(2)
1
```

### Interests of tuples

Tuples are useful because they are:

- faster than lists
- protect the data, which is immutable
- tuples can be used as keys on dictionaries

In addition, they can be used in different useful ways:

Tuples can be used as **key/value pairs to build dictionaries**

```python
>>> d = dict([('jan', 1), ('feb', 2), ('march', 3)])
>>> d['feb']
2
```

Tuples can be used for **assigning multiple values**

```python
>>> (x,y,z) = ('a','b','c')
>>> x
'a'
>>> (x,y,z) = range(3)
>>> x
0
```

Likewise they're great for **unpacking**

```python
>>> data  = (1,2,3)
>>> x, y, z = data
>>> x
1
```

### find the length of a tuple

To find the length of a tuple, you can use the `len()` function:

```python
>>> t= (1,2)
>>> len(t)
2
```

### Slicing (extracting a segment)

```python
>>> t = (1,2,3,4,5)
>>> t[2:]
(3, 4, 5)
```

### Math and comparison

comparison operators and mathematical functions can be used on tuples

```python
>>> t = (1, 2, 3)
>>> max(t)
3
```

## Dictionaries

A dictionary is a sequence of items.
Each item is a pair made of a key and a value
Dictionaries are not sorted. You can access the list of keys or the list of values independently

```python
>>> d = {'first':'string value', 'second':[1,2]}
>>> d.keys()
['first', 'second']
>>> d.values()
['string value', [1, 2]]
```

You can access the value of a given key as follows:

```python
>>> d['first']
'string value'
```

### Methods to query information

In addition to **keys** and **values** methids, there it also **items** method

**items()** returns a list of items of the form **(key, value)**

The items are not return in any particular order:

```python
>>> d = {'first':'string value', 'second':[1,2]}
>>> d.items()
[('a', 'string value'), ('b', [1, 2])]

>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.items())
[('a', 10), ('b', 20), ('c', 30)]
>>> list(d.items())[1][0]
'b'
>>> list(d.items())[1][1]
20
```

The **iteritems** method works in much the same way, **but** returns an **iterator** instead of a list

```python
>>> [x for x in t.itervalues()]
['string value', [1, 2]]
>>>
>>> [x for x in t.iterkeys()]
['first', 'csecond']
>>> [x for x in t.iteritems()]
[('a', 'string value'), ('b', [1, 2])]
```

You can check for the existence of a specific key with **has_key:**

```python
>>> d.has_key('first')
True
```

The expression **d.has_key(k)** is equivalent to **k in d**
The choice of which to use is largely a matter of taste

In order to get the value corresponding to a specific key, use **get** or **pop**:

```python
>>> d.get('first')  # this method can set an optional value, if the key is not found
'string value'
```

`d.get()` returns the value for a key if it exists in the dictionary

```python
>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> print(d.get('b'))
20
>>> print(d.get('z'))
None
```

It is useful for things like adding up numbers:
`sum[value] = sum.get(value, 0) + 1`

The difference between `get` and `pop` is that `pop` also removes the corresponding item from the dictionary:

`pop():` Removes a key from a dictionary, if it is present, and returns its value.

```python
>>> d.pop('first')
'string value'
>>> d
{'second': [1, 2]}

>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.pop('b')
20
>>> d
{'a': 10, 'c': 30}
```

Finally, `popitem` removes and returns a pair (key, value)
you do not choose which one because a dictionary is not sorted

```python
>>> d.popitem()
('a', 'string value')
>>> d
{'second': [1, 2]}
```

## Sets

### Creating Python Sets

A set is created by placing all the items (elements) inside curly braces `{}`, separated by comma, or by using the built-in `set()` function.

sets **cannot** have mutable elements like `lists` or `sets` or `dictionaries` as its elements

```python
# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
```

Output: `{1, 2, 3}` & `{1.0, (1, 2, 3), 'Hello'}`

### Modifying a set in Python

Sets are mutable. However, since they are unordered, indexing has no meaning.

We cannot access or change an element of a set using indexing or slicing.
Set data type does not support it.

We can add a single element using the `add()` method
Multiple elements using the `update()` method.
The `update()` method can take tuples, lists, strings or other sets as its argument
**In all cases, duplicates are avoided.**

```python
# initialize my_set
my_set = {1, 3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

# my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)
```

Output:

```python
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}
```

### Removing elements from a set

A particular item can be removed from a set using the methods `discard()` and `remove()`

The only difference between the two is:
`discard()` function leaves a set unchanged if the element is not present in the set

On the other hand, the `remove()` function will raise an error in such a condition (if the element is not present in the set)

```python
# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)
```

Output:

```python
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
Traceback (most recent call last):
  File "<string>", line 28, in <module>
KeyError: 2
```

Similarly, we can remove and return an item using the `pop()` method

Since set is an unordered data type, **there is no way of determining which item will be popped**. It is completely arbitrary

We can also remove all the items from a set using the `clear()` method

```python
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

print(my_set)
```

Output:

```python
{'H', 'l', 'r', 'W', 'o', 'd', 'e'}
H
{'r', 'W', 'o', 'd', 'e'}
set()
```

### Python Set Operations

Set can be used to carry out mathematical set operations like `union`, `intersection`, `difference` and `symmetric` difference. We can do this with operators or methods

Let us consider the following two sets for the following operations

```python
>>> A = {1, 2, 3, 4, 5}
>>> B = {4, 5, 6, 7, 8}
```

Union of `A` and `B` is a set of all elements from both sets

Union is performed using `|` operator. Same can be accomplished using the `union()` method

```python
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
```

Output: `{1, 2, 3, 4, 5, 6, 7, 8}`

**Intersection** of **A** and **B** is a set of elements that are common in both the sets.

Intersection is performed using **&** operator. Same can be accomplished using the **`intersection()`** method

```python
# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# use intersection function on A
>>> A.intersection(B)
{4, 5}

# use intersection function on B
>>> B.intersection(A)
{4, 5}
```

Output: `{4, 5}`

**Difference** of the set `B` from set `A`(`A` - `B`) is a set of elements that are only in `A` but not in `B`. Similarly, `B` - `A` is a set of elements in `B` but not in `A`.

Difference is performed using `-` operator. Same can be accomplished using the `difference()` method.

```python
# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# use difference function on A
>>> A.difference(B)
{1, 2, 3}

# use - operator on B
>>> B - A
{8, 6, 7}

# use difference function on B
>>> B.difference(A)
{8, 6, 7}
```

Output: `{1, 2, 3}`

**Symmetric Difference** of `A` and `B` is a set of elements in `A` and `B` but not in both (excluding the intersection).

**Symmetric difference** is performed using `^` operator. Same can be accomplished using the method `symmetric_difference()`

```python
# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
>>> A.symmetric_difference(B)
{1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
>>> B.symmetric_difference(A)
{1, 2, 3, 6, 7, 8}
```

Output: `{1, 2, 3, 6, 7, 8}`

## heapq

**Heaps** and **Priority Queues** are amazing for **finding the best element in a dataset** problems. Because they're easy to use and highly effective

The python **heapq** module is part of the standard library.
It implements all the low-level heap operations as well as some high-level common uses for heaps

A **priorirty-queue** is a powerful tool that can solve problems as varied as:

- writing an email scheduler
- **finding the shortest path on a map**
- merging log files

### What are heaps

**`heapq`** is a **binary heap**, with `O(log n)` **push** and `O(log n)` **pop**

Heaps are **concerte** data structures, where as priority queues are **abstract** data structures

An **abstract** data structure determines the **interface**, while a concrete data structure defines the implementation

**Heaps** are commonly used to implement priority queues

**Concrete data structures** also specify **performance guarantees**
Performance guarantees define the relationship between the size of the structure and the time operations take

The priority queue supports 3 operations:

1. `is_empty` checks whether the queue is empty
2. `add_element` adds an element to the queue
3. `pop_element` pops the element with the highest priority

Priority queues are commoing used for optimizing task execution, in which the goal is to work on the task with the highest priority
After a task is completed, its priority is lowered, and it's returned to the queue

There are **2 different conventions fo determining the priority of an element:**

1. The *largest* element has the highest priority
2. The *smallest* element has the highest priority

These two conventions are equivalent because you can always reverse the effective order

The Python *heapq* useds the second convention (smallest has highest priority) -- And it's usually the most useful of the 2 conventions

The heap implementation of the priority queue guarantees that both **pushing (adding)** and **popping (removing)** elements are **logarithmic time** operations
This means that the **time it takes to do push and pop is proportional to the base-2 logarithm of the number of elements**

### Uses of Priority Queues

A priority queue, and a heap as an implementation of a priority queue is useful for programs that involve finding an element that is extreme in some way.

- Gettings the three most popular blog posts from hit data
- Finding the fastest way to get from one point to the other
- Predicting which bus will be the first to arrive at a station based on arrival frequency

### Heaps as Lists in the Python *heapq* module

A heap queue is created by using Python's inbuilt library named `heapq`
This library has the relevant funtions to carry out various operations on a heap data structure, below is a list of these functions

- `heapify`: this function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted
- `heappush`: this function adds an element to the heap without altering the current heap
- `heappop`: this function returns the smallest data element from the heap
- `heapreplace`: this functin repalces the smallest data element with a new value supplied in the function

### Creating a heap

A heap is created by simply using a list of elements with the heapify function.
In the below example we supply a list of elements and the heapify function rearranges the elements bringing the smallest element to the first position

```python
import heapq
H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
```

Output: `[1, 3, 5, 78, 21, 45]`

**Inserting** a data element to a heap always adds the element at the last index
But you can apply heapify function again to bring the newly added element to the first index only if it's the smallest in value

```python
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)
```

Output:

```python
[1, 3, 5, 78, 21, 45]
[1, 3, 5, 78, 21, 45, 8]
```

**Removing from heap:** You can remove the element at first index by using this function

```python
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)
```

Output:

```python
[1, 3, 5, 78, 21, 45]
[3, 21, 5, 78, 45]
```

**Replacing in a heap...** the `heapreplace` function always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order

```python
import heapq
H = [21,1,45,78,3,5]
# Create the heap
heapq.heapify(H)
print(H)
# Replace an element
heapq.heapreplace(H,6)
print(H)
```

Output:

```python
[1, 3, 5, 78, 21, 45]
[3, 6, 5, 78, 21, 45]
```
