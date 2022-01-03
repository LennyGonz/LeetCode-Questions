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

# Given the head of a Linked List and a number 'k', reverse every 'k' sized sub-list start from the head

def reverse_every_k_elements(head, k):
  if k <= 1 or head is None:
    return head
  
  current = head
  previous = None
  
  while current is not None:
    last_node_of_previous_part = previous
    
    last_node_of_sub_list = current
    
    i=0
    while current is not None and i < k:
      next = current.next 
      current.next = previous
      previous = current
      current = next
      i += 1
    
    if last_node_of_previous_part is not None:
      last_node_of_previous_part.next = previous
    else:
      head = previous
    
    last_node_of_sub_list.next = current
    
    previous = last_node_of_sub_list
  
  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)
  
  print("Nodes of original Linked List are: ", end='')
  head.print_list() # 12345678
  
  result = reverse_every_k_elements(head,3)
  print("Nodes of reversed Linked List are: ", end='')
  result.print_list() # 32165487

main()
