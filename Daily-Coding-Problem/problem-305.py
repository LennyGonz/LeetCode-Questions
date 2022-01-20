class LinkedList:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def print_nodes(ll):
  start = end = ll

  while start:
    end = start
    total = 0
    skip = False

    while end:
      total += end.data
      if total == 0:
        start = end
        skip = True
        break
      end = end.next

    if not skip:
      print(start.data)

    start = start.next

'''
In the worst case, we must move our end pointer across the remainder of the linked list for each potential start node, taking O(N2) time.

At any given time we will only be tracking the two pointers and our running total, so the total space required is O(1).
'''
