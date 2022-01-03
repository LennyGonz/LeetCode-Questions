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
  

def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  last_node = head
  list_length = 1
  
  while last_node.next is not None:
    last_node = last_node.next
    list_length += 1
  
  last_node.next = head
  
  rotations %= list_length
  skip_length = list_length - rotations
  
  last_node_of_rotated_list = head
  for i in range(skip_length - 1):
    last_node_of_rotated_list = last_node_of_rotated_list.next
  
  head = last_node_of_rotated_list.next
  
  last_node_of_rotated_list.next = None
  
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
  
  result = rotate(head,4)
  print("Nodes of reversed Linked List are: ", end='')
  result.print_list() # 56781234

main()
