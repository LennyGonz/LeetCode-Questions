from recursion.add_two_numbers import ListNode


def addTwoNumbers(l1, l2):
  res = l1.val + l2.val
  digit = res % 10
  carry = res // 10
  answer = ListNode(digit)

  if any((l1.next, l2.next, carry)):
    l1 = l1.next if l1.next else ListNode(0)

    l2 = l2.next if l2.next else ListNode(0)

    answer.next = addTwoNumbers(l1, l2)
  
  return answer

