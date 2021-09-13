def swap_every_two(node):
  curr = node

  while curr and curr.next:
    curr.val, curr.next.val = curr.next.val, curr.val
    curr = curr.next.next
  return node
