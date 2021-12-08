# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def addTwoNumbers(l1, l2):
  carry = 0
  root = n = ListNode(0)
  print(root)
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
