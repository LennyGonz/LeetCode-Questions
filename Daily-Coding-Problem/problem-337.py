import random
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def shuffle(head):
  def length(l):
    """Returns the number of nodes in a list."""
    count = 0
    while l:
      l = l.next
      count += 1
    return count

  def last(l):
    """Returns the last node of a list."""
    while l.next:
      l = l.next
    return l

  def merge(left, right):
    left_len = length(left)
    right_len = length(right)
    dummy = Node(0)
    curr = dummy
    while left or right:
      r = random.random()
      # Choose the threshold based on the proportion of the length
      # of the left list to the total length of the remaining list.
      if r < left_len / (left_len + right_len):
        # Add to the new list from the left
        curr.next = left
        left = left.next
        left_len -= 1
      else:
        # Add to the new list from the right
        curr.next = right
        right = right.next
        right_len -= 1
      curr = curr.next

    ## These checks are taken care of by the above threshold
    # if left:
    #     curr.next = left
    # if right:
    #     curr.next = right

    return dummy.next

  size = length(head)
  if size <= 1:
    return head

  dummy = Node(0)
  dummy.next = head
  # Start with a window size of 1, growing by a factor of 2 each time.
  window = 1
  while window < size:
    prev_list = dummy
    curr = dummy.next
    while curr:
      # Isolate the left sublist as `left`
      left = curr
      prev = None
      right = left
      for _ in range(window):
        if right is None:
          break
        prev = right
        right = right.next
      prev.next = None
      # Isolate the right sublist as `right`
      curr = right
      for _ in range(window):
        if curr is None:
          break
        prev = curr
        curr = curr.next
      prev.next = None
      # Merge the two sublists
      merged = merge(left, right)
      # Add back into the list in the correct location
      prev_list.next = merged
      prev_list = last(merged)

    window *= 2

  return dummy.next
