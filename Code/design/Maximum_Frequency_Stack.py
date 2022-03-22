'''
LeetCode #895

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

- FreqStack() constructs an empty frequency stack.
- void push(int val) pushes an integer val onto the top of the stack.
- int pop() removes and returns the most frequent element in the stack.
  - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

----------------------------------------------------------------------------------------------------------------------------------------------------------
My immediate thought is to use a heap, because a max heap's root is the greatest element in the heap

Each heap node will consist of: (count, index, number) in min-heap and keeping map of counts.
Since its a min-heap, I am negating the count and index while pushing in the heap.

The intuition is, heap will always keep the element with max count on top, and if two elements have same count,
the second element (index) will be considered while doing pop operation.
Also, the count map, is useful when the new occurence of the exisiting element is pushed.

* Since python doesn't natively do max-heaps I am negating the count and index while pushing in the heap in order to implement the max-heap
* more optimal solution at the bottom
'''
from collections import defaultdict, Counter
from heapq import *

class FreqStack:
  def __init__(self):
    self.heap = []
    self.m = defaultdict(int)
    self.index = 0

  def push(self, x):
    self.m[x]+=1
    heappush(self.heap,(-self.m[x], -self.index, x))
    self.index+=1
  
  def pop(self):
    toBeRemoved = heappop(self.heap)
    self.m[toBeRemoved[2]]-=1
    return toBeRemoved[2]

'''
Time complexity is O(NlogN) to maintain the heap
Space complexity is O(N) - holds N elements in the worst case

* THIS CAN BE IMPROVED
'''
def main():
  obj = FreqStack()
  
  print(obj.push(5))
  print(obj.push(7))
  print(obj.push(5))
  print(obj.push(7))
  print(obj.push(4))
  print(obj.push(5))
  print(obj.pop())
  print(obj.pop())
  print(obj.pop())
  print(obj.pop())
  '''
  the heap [(-1, 0, 5)]
  the heap [(-1, -1, 7), (-1, 0, 5)]
  the heap [(-2, -2, 5), (-1, 0, 5), (-1, -1, 7)]
  the heap [(-2, -3, 7), (-2, -2, 5), (-1, -1, 7), (-1, 0, 5)]
  the heap [(-2, -3, 7), (-2, -2, 5), (-1, -1, 7), (-1, 0, 5), (-1, -4, 4)]
  the heap [(-3, -5, 5), (-2, -2, 5), (-2, -3, 7), (-1, 0, 5), (-1, -4, 4), (-1, -1, 7)]
  toBeRemoved (-3, -5, 5)
  pop heap [(-2, -3, 7), (-2, -2, 5), (-1, -1, 7), (-1, 0, 5), (-1, -4, 4)]
  toBeRemoved (-2, -3, 7)
  pop heap [(-2, -2, 5), (-1, -4, 4), (-1, -1, 7), (-1, 0, 5)]
  toBeRemoved (-2, -2, 5)
  pop heap [(-1, -4, 4), (-1, 0, 5), (-1, -1, 7)]
  toBeRemoved (-1, -4, 4)
  pop heap [(-1, -1, 7), (-1, 0, 5)]
  
  [null,null,null,null,null,null,null,5,7,5,4]
  '''

main()

'''
We need to track the frequency of an element
Let freq be a Map from x to the number of occurrences of x

We also NEED to know the current maximum frequency of any element in the stack (for the pop function) 

The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent?
We can use a stack to query this information: the top of the stack is the most recent.

To this end, let "group" be a map from frequency to a stack of elements with that frequency. We now have all the required components to implement FreqStack.

Hash map freq will count the frequence of elements.
Hash map m is a map of stack -> we use a default dict, where the key is the number of frequencies, and the value is a list of elements that appear "key times"
'''
class FreqStack(object):
  def __init__(self):
    # dictionary freq will count the frequency of elements
    self.freq = Counter()
    
    # m is a map of our stack
    self.m = defaultdict(list)
    
    # maxfreq records the maximum frequence.
    self.maxf = 0

  def push(self, x):
    # this line is to just make the code more legible
    freq, m = self.freq, self.m
    
    # increase the frequency of the current element
    freq[x] += 1
    
    # we need to update the max frequency
    self.maxf = max(self.maxf, freq[x])
    
    # here we map the frequency to a stack of elements with that frequency...
    m[freq[x]].append(x)

  def pop(self):
    # again this line is to just make the code more legible
    freq, m, maxf = self.freq, self.m, self.maxf
    
    # x will hold the most frequent element
    # we need to know the maximum frequence, so use that as the key, and pop the most frequent element
    x = m[maxf].pop()
    
    # we need to update maxF
    # if the maximum frequence was 5, but only 1 element had a frequency of 5
    # we need to decrease maximum frequence
    if not m[maxf]: self.maxf = maxf - 1
    
    # we need to update our frequency map every time we pop
    freq[x] -= 1
    
    # return the element we just popped
    # which is the most frequent
    return x

'''
Complexity Analysis

Time Complexity: O(1) for both push and pop operations.

Space Complexity: O(N), where N is the number of elements in the FreqStack.
'''

'''
map of stack:  defaultdict(<class 'list'>, {1: [5]})
freq Counter({5: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7]})
freq Counter({5: 1, 7: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7], 2: [5]})
freq Counter({5: 2, 7: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7], 2: [5, 7]})
freq Counter({5: 2, 7: 2})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7, 4], 2: [5, 7]})
freq Counter({5: 2, 7: 2, 4: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7, 4], 2: [5, 7], 3: [5]})
freq Counter({5: 3, 7: 2, 4: 1})

# HERE WE BEGIN TO POP
map of stack:  defaultdict(<class 'list'>, {1: [5, 7, 4], 2: [5, 7], 3: []})
freq Counter({5: 2, 7: 2, 4: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7, 4], 2: [5], 3: []})
freq Counter({5: 2, 7: 1, 4: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7, 4], 2: [], 3: []})
freq Counter({5: 1, 7: 1, 4: 1})

map of stack:  defaultdict(<class 'list'>, {1: [5, 7], 2: [], 3: []})
freq Counter({5: 1, 7: 1, 4: 0})
'''
