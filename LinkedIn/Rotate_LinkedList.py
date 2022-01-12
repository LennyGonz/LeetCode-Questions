'''
Another way of defining the rotation is to take the sub-list of 'k' ending nodes of the LinkedList 
AND connect them to the beginning. 

Other than that we have to do three more things:

1. Connect the last node of the LinkedList to the head, because the list will have a different tail after the rotation.

2. The new head of the LinkedList will be the node at the beginning of the sublist.

3. The node right before the start of sub-list will be the new tail of the rotated LinkedList.

In the position n - k, where n is a number of nodes in the list. 

The new tail is just before the new head, in the position n - k.

example:
input: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null and k=3 
output: head -> 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> null

n = 6 and k = 3 -> node at position 3 is the new tail (n-k) and the new head is (n-k+1)

Notice that the sub-list of k ending nodes is: 4 -> 5 -> 6 | 4 will be our new head & 3 will be our new tail

To do this, we need to first find the length of the linked list
In addition to finding the length of the linked list, we can leave a pointer at the tail node, 
this will allow us to make the tail node point to the head
Creating a cycle

Once we have the length of the linked list, this will allow me to calculate the skip length

Find element where we need to cut our list: it has number n - k%n, but we need to cut previous connection, so we stop one element earlier

I need the skip length to be able to traverse till the new tail of the rotated linked list

Once I have a pointer at the new tail

I redefine head to be new_tail.next (which is the head)

Then make the tail a tail, by making new_tail.next point to None

THATS IT!

AND since we redefined head, we can return head
'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def rotated(head, k):
	# base cases - if we're given an empty linked list, or just a head node -> return head
  # if k <= 0, we do not need to rotate list, so return it as it is.
	if head is None or head.next is None or k <= 0:
		return head
	
	# we want to leave a pointer at the last node - this will help connect the last node to head
	last_node = head
	
	# we calculate the length, bc later it will help us determine how nodes we can traverse to land on the new tail and new head
  # we can initialize it to 1, because 1 is head
	list_length = 1
	
  # traverse the linked list till we reach the end
	while last_node.next is not None:
		last_node = last_node.next
		list_length += 1
	
	# create the cycle
	last_node.next = head
	
	# there will be also be cases where k(# of rotations) is greater than the length of the input linked list,
  # this calculation helps calculate the correct skip length
	k %= list_length
	skip_length = list_length - k
	
	# we create another pointer that will point at the new tail and point to the new head
	new_tail = head
	
  # make the new pointer new_tail traverse (skip_length-1) nodes
	for _ in range(skip_length - 1):
		new_tail = new_tail.next
	
	# Our traversal will land our pointer on the new tail of the rotated linked list, and it's also still pointing to the new head. So we can redefine head
	head = new_tail.next
	
	# then we define the next pointer of our new tail to none
	new_tail.next = None
	
	return head

'''
Time: O(N), where 'N' is the total number of nodes in the input linkedlist & we do this in 1-pass
Space: O(1), algorithm runs in constant space
'''
