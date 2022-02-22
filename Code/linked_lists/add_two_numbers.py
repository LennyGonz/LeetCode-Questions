# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
'''
LeetCode Question #2 Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

----------------------------------------------------------------------------------------------

There are a lot of edge cases with this problem

When you're adding 2 numbers - problem says both numbers are NON-EMPTY so we know we won't ever have a 500 + null situation

Having the inputs in reverse order is actually helpful ...

5 -> 6 -> 4
2 -> 4 -> 3 -> 3

When you add, you start by adding the numbers in the 1s place... so with them being in reverse order. It's very easy to begin the addition

5 -> 6 -> 4                                                   another example:   _  7
2 -> 4 -> 3 -> 3                                                               +  _ 8
----------------                                                               --------
7    0    8(carry of 1) 3 -> 465 + 3342 = 3807                                    15 -> we know it's 15 but the carry has no node to add with SO we need to remember to include the carry in our algorithm
'''

def addTwoNumbers(l1, l2):
  #resulting linked list
  dummy = ListNode()
  
  # curr pointer is going to point at the position we're inserting the new digit
  curr = dummy

  # need a variable to hold our carry
  carry = 0
  
  # we have to iterate thru either list as long as one list still has digits to go through
  # if we're adding 7+8 -> carry will hold a digit -> so we need to keep the loop going
  while l1 or l2 or carry:
    # digit from list 1
    # v1 will be the digit from list 1 IF there even is a digit left in list 1 ELSE the list is null (bc we iterated through the entirity of it) so v1 will be 0
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    
    # new digit (basic addition)
    val = v1 + v2 + carry
    
    # BUT if val has 2 digits - we need to extract the carry
    carry = val // 10
    
    # IF the value is 2 digits we want val to hold the digit in the ones place
    val = val % 10
    
    # we need to insert the value into our result list
    curr.next = ListNode(val)
    
    # update pointer
    curr = curr.next
    
    # update list pointers
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    
  return dummy.next

'''
Time: O(N + M) -> where N and M is the number of nodes in each list & each list is traversed a single time
Space: O(1) -> the algorithm runs in constant time
'''

# same algorithm just different
def addTwoNumbers(l1, l2):
  carry = 0
  root = n = ListNode(0)
  while l1 or l2 or carry:
    v1 = v2 = 0
    if l1:
      v1 = l1.val
      l1 = l1.next
    if l2:
      v2 = l2.val
      l2 = l2.next
    carry, val = divmod(v1+v2+carry, 10)
    n.next = ListNode(val)
    n = n.next
  return root.next

'''
Output for test run on this example: l1 = [2,4,3] & l2 = [5,6,4]

ListNode{val: 0, next: None}
v1: 2
l1: ListNode{val: 4, next: ListNode{val: 3, next: None}}
****
v2: 5
l2: ListNode{val: 6, next: ListNode{val: 4, next: None}}
----
carry: 0 |||| val: 7
n.next ListNode{val: 7, next: None}
n: ListNode{val: 7, next: None}
-------------------------------------------
v1: 4
l1: ListNode{val: 3, next: None}
****
v2: 6
l2: ListNode{val: 4, next: None}
----
carry: 1 |||| val: 0
n.next ListNode{val: 0, next: None}
n: ListNode{val: 0, next: None}
-------------------------------------------
v1: 3
l1: None
****
v2: 4
l2: None
----
carry: 0 |||| val: 8
n.next ListNode{val: 8, next: None}
n: ListNode{val: 8, next: None}
-------------------------------------------
root ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}}
'''

## Recursive Solution

def addTwoNumbers(self, l1: ListNode, l2: ListNode):
  res = l1.val + l2.val

  # seperate the double digit value
  digit, tenth = res % 10, res // 10

  # answer is the resulting linked list
  answer = ListNode(digit)

  # The any() function returns True if any element of an iterable is True. If not, any() returns False.
  if any((l1.next, l2.next, tenth)):
    # if the list is not empty - l1 is the value of the node OTHERWISE l1's value is 0
    l1 = l1.next if l1.next else ListNode(0)
    l2 = l2.next if l2.next else ListNode(0)
    l1.val += tenth
    
    # recursive call to build the linked list
    answer.next = self.addTwoNumbers(l1, l2)

  return answer

'''
Time: O(N+M)
Space: O(N) - # of recursive calls on the call stack
'''
