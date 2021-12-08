from __future__ import print_function
'''
Reverse a Linked List (easy)
Given the head of a Singly LinkedList, reverse the LinkedList
Write a function to return the new head of the reversed LinkedList

Time = O(N) -> where N represents the total number of nodes in the LinkedList
Space = O(1) -> No extra memory is used
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse(head):
  previous = None
  current = head
  next = None
  
  while current is not None:
    
    next = current.next
    
    current.next = previous
    
    previous = current
    
    current = next
  
  return previous

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  
  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

main()
