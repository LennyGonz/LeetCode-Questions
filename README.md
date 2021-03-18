# LeetCode-Questions

* Code
* Code walkthroughs

Also contains a python refresher

<hr>

| Problem Number | Problem Name | Solution | Difficulty |
| :--: | :--: | :--: | :--: |
| 1 | Two Sums | [Code](Code/two_sum.py) & [Walk-Through](PDFs/Two%20Sums.pdf) | Easy
| 2 | Add Two Numbers | [Code](Code/longest_substring.py) & [Walk-Through](PDFs/Add%20Two%20Numbers.pdf) | Medium
| 3 | Longest Substring Without Repeating Characters | [Code](Code/longest_substring_2.py) & [Walk-Through](PDFs/Longest%20Substring%20without%20Repeating%20Characters%20V2.pdf) | Medium
| 3 | Longest Substring Without Repeating Characters | Alternate Solution <br> [Code](Code/longest_substring.py) & [Walk-Through](PDFs/Longest%20Substring%20without%20Repeating%20Characters.pdf) | Medium
| 4 | Median of Two Sorted Arrays | [Code](Code/median_of_two_sorted_arrays.py) & [Walk-Through](https://www.youtube.com/watch?v=LPFhl65R7ww) | Hard
| 5 | Longest Palindromic Substring | [Code](Code/longest_palindromic_substring.py) & [Walk-Through] | Medium
| 6 | ZigZag Conversion | [Code](Code/zigzag_conversion.py) & [Walk-Through](PDFs/Zig-Zag%20Conversion.pdf) | Medium
| 7 | Reverse Integer | [Code](Code/reverse_integer.py) & [Walk-Through] | Easy
| 8 | String to Integer (atoi) | [Code](Code/string_to_integer.py) & [Walk-Through] | Medium
| 9 | Palindrome Number | [Code](Code/palindromeNumber.py) & [Walk-Through](PDFs/Palindrome%20Number.pdf) | Easy

<hr>

Problem 46

Permutations | [Code](Code/permutations.py) | [Walk-Through]

<hr>

Problem 141

Linked List Cycle | [Code](Code/detect_linkedlist_cycle.py) | [Walk-Through](PDFs/Linked%20List%20Cycle.pdf)

<hr>

Problem 929

Unique Email Address | [Code](Code/unique_email_address.py) | [Walk-Through](PDFs/Unique%20Email%20Address.pdf)

<hr>

# Daily Coding Challenge

Problem 1

Given a list of numbers, return whether any two sums to k.

For example, given [10,15,3,7] and k of 17, return `true` since `10 + 7 = 17`

Bonus: Can you do this in one pass?

[Solution](Daily-Coding-Problem/problem-1.py)

<hr>

Problem 2

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i

For example, given `[1,2,3,4,5]`, the expected output would be `[120,60,40,30,24]`.
<br>
If our input was `[3,2,1]`, the expected output would be `[2,3,6]`

*Follow-up:* What if you can't use division?

[Solution](Daily-Coding-Problem/problem-2.py)

<hr>

Problem 3

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserializes(s)`, which deserializes the string back into the tree.

For example, given the following `Node` class

```python
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert (deserialize(node)).left.left.val == 'left.left'
```

<hr>

problem 4

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input `[3,4,-1,1]` should give `2`.
The input `[1,2,0]` should give `3`

You can modify the input array in-place

<hr>

problem 5

*Throwback to Scheme/Lisp*

`cons(a,b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair.
For example, `car(cons(3,4))` returns `3` and `cdr(cons(3,4))` returns `4`

Given this implementation:

```python
def cons(a, b):
  return lambda f: f(a, b)
```

Implement `car` and `cdr`

<hr>

problem 6

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

<hr>

problem 7

Give the mapping a = 1, b = 2, c = 3, d = 4, e = 5 ... z = 26, and an encoded message, count the number of ways it can be decoded

For example, the message `'111'` would give 3, since it could be decoded as 'aaa', 'ka', 'ak'
You can assume that the messages are decodable. For example, '001' is not allowed

<hr>

problem 8


<hr>
