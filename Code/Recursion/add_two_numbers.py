# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    res = l1.val + l2.val
    digit, tenth = res % 10, res // 10
    answer = ListNode(digit)

    # The any() function returns True if any element of an iterable is True. If not, any() returns False.
    if any((l1.next, l2.next, tenth)):
      l1 = l1.next if l1.next else ListNode(0)
      l2 = l2.next if l2.next else ListNode(0)
      l1.val += tenth
      answer.next = self.addTwoNumbers(l1, l2)    
    return answer

print(Solution.addTwoNumbers([1,2,3],[4,5,6]))
