from __future__ import print_function

class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next
  
  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end="")
      temp = temp.next
    print()

# Given the head of a Linked List and two positions "p" and "q", reverse the Linked List from position "p" to "q"

def reverse_sub_list(head,p,q):
  if p == q:
    return head
  
  current = head
  previous = None
  
  i = 0
  while current is not None and i < p-1:
    previous = current
    current = current.next
    i += 1
  
  last_node_of_first_part = previous
  last_node_of_sub_list = current
  
  i = 0
  while current is not None and i < q-p+1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1
  
  if last_node_of_first_part is not None:
    last_node_of_first_part.next = previous
  else:
    head = previous
  
  last_node_of_sub_list.next = current

  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  
  print("Nodes of original Linked List are: ", end='')
  head.print_list() # 12345
  
  result = reverse_sub_list(head,2,4)
  print("Nodes of reversed Linked List are: ", end='')
  result.print_list() # 14325

main()
