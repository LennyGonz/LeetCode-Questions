class LinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None

def alternate(ll):
  prev = ll
  curr = ll.next

  while curr:
    if prev.data > curr.data:
      prev.data, curr.data = curr.data, prev.data

    if not curr.next:
      break

    if curr.next and curr.next.data > curr.data:
      curr.next.data, curr.data = curr.data, curr.next.data

    prev = curr.next
    curr = curr.next.next

  return ll

'''
Both of these algorithms use O(N) time and O(1) space, since we must traverse the entire linked list, and we are only tracking one or two nodes at a time.
'''
