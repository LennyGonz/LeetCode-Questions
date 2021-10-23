class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, data):
    if not self.head:
      self.head = self.tail = Node(data)
    else:
      tmp = Node(data)
      tmp.next = self.head
      self.head = tmp

  def append(self, data):
    if not self.head:
      self.head = self.tail = Node(data)
    else:
      tmp = Node(data)
      self.tail.next = tmp
      self.tail = self.tail.next
