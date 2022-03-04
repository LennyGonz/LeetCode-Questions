'''
LeetCode #445

You are given two non-empty linked lists representing two non-negative integers.

The most significant digit comes first and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

----------------------------------------------------------------------------------------------
The problem is a combination of three basic problems:

Reverse Linked List.

Add Strings - the good problem to refresh textbook digit-by-digit addition algorithm.

Add Two Numbers - the same problem as the current one, but the digits are stored in reverse order
----------------------------------------------------------------------------------------------

What immediately comes to mind, is to traverse both lists and append each into a stack

1. Iterate over the first and the second lists and create two stacks: st1 and st2.
2. Iterate over stacks, 
    - pop last elements from stack if possible, 
    - if not, use 0 for empty stack. 
      - Add these two numbers and evaluate next digit and carry. 
      - Create new node with digit and attach it before current head, update head.
3. Just return head in the end.

Complexity: time and space complexity is O(m+n), where m and n lengths of our lists.
'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def addTwoNumbers(self, l1, l2):
  # a stack for each list
  st1, st2 = [], []
  
  # traverse the first list -> appending each node to its respective stack
  while l1:
    st1.append(l1.val)
    l1 = l1.next

  # traverse the second list -> appending each node to its respective stack
  while l2:
    st2.append(l2.val)
    l2 = l2.next
  
  # these will be necessary for the resulting summation
  carry, head = 0, None

  # we start adding the 2 numbers
  while st1 or st2 or carry:
    # identify the 2 numbers we're about to add
    d1, d2 = 0, 0
    # requires popping the node off the stack - if there is a node left to pop else use 0
    d1 = st1.pop() if st1 else 0 
    d2 = st2.pop() if st2 else 0
    
    # instead of divmod we can do this
    # new digit (basic addition)
    digit = d1 + d2 + carry
    # BUT if val has 2 digits - we need to extract the carry
    carry = digit // 10
    # IF the value is 2 digits we want val to hold the digit in the ones place
    digit = digit % 10
    
    # divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
    # If x and y are integers, the return value from divmod() is same as (a // b, x % y
    #carry, digit = divmod(d1 + d2 + carry, 10)
    
    # remember we're adding right to left
    # we're initially starting with the tail pointing to None
    # Then we shift head to become the new node we created
    # so in the end -> head will be the most significant digit
    head_new = ListNode(digit)
    head_new.next = head
    head = head_new

  return head
