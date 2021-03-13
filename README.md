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

