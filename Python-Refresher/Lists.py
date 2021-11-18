'''
Arrays in Python are called lists:

list.append(x) -- Add an item to the end of the list

list.extend()

list.insert()

list.remove()

list.pop([])

list.clear()

list.index(x[,start[,end]])

list.count()

list.sort(key=None, reverse=False)

list.reverse() --> reverse the elements of this list in place

list.copy()

Using Lists as Stacks
* Remember stacks are (Last-In, First-Out):

To add an item to the top of the stack, use append()

To retrieve an item from the top of the stack use pop()

Using Lists as Queues
* Remember queues are (First-In, First-Out):
* Lists are not efficient for this purpose

To add an item to the queue, use append()

To remove an item from the queue, use popleft()

'''

from collections import Counter
words = "hello my name is Lenny hello name hello what".split()
c = Counter(words)
print(c)