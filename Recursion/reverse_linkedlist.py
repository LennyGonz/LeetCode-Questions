class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def reverseLinkedList(head):
  # base cases
  # if linked list is empty or the linked list has a single node - return head
  if head is not None or head.next is None:
    return head

  # traverse to the end of the linked list and when we reach the end node we label it: newHead
  newHead = reverseLinkedList(head.next)
  
  # we start flipping pointers - by creating a cycle
  head.next.next = head
  
  # we break the cycle - and when we reach the former head node - we make its pointer point to None
  head.next = None
  
  return newHead

# Recursive Python3 program to reverse
# a linked list
import math

# Link list node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
def LinkedList():
	head = None
		
# Function to reverse the linked list
def reverse(node):
	if (node == None):
		return node
		
	if (node.next == None):
		return node
		
	node1 = reverse(node.next)
	node.next.next = node
	node.next = None
	return node1

# Function to print linked list
def printList():
	temp = head
	while (temp != None):
		print(temp.data)
		temp = temp.next

def push(head_ref, new_data):
	new_node = Node(new_data)
	new_node.data = new_data
	new_node.next = head_ref
	head_ref = new_node
	return head_ref

# Driver Code
if __name__=='__main__':
	
	# Start with the empty list
	head = LinkedList()
	head = push(head, 4)
	head = push(head, 3)
	head = push(head, 2)
	head = push(head, 1)

	print("Given linked list")
	printList()

	head = reverse(head)

	print("\nReversed Linked list")
	printList()
	
# This code is contributed by AbhiThakur

