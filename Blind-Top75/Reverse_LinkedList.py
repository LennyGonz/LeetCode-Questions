'''
Leetcode #206

Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
_____________________________________________________________________________________________________________________________________________________

There are 2 approaches to this:

1) iteratively - Time: O(N) because we traverse every node & Space: O(1) because the algorithm runs in constant time
2) Recursively - Time: O(N) because we traverse every node & Space: O(N) because the call stack has N recursive calls

To reverse a LinkedList, we need to reverse one node at a time.

1) We will start with at the head, which is pointing to the head of the LinkedList and a variable previous which will point to the previous node that we have processed; 
  * Initially previous will point to null.

2) In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next node.

3)Also, we will update the previous to always point to the previous node that we have processed.
'''
def reverselist(head):
  previousNode = None
  # we need to traverse the array whilst simultanously reversing the list

  # while there's a VALID head node keep the loop going
  # if we did while head.next (this would end 1 iteration too early)
  # while there is a valid head keep going (once we reach the end of the linkedlist head=None and exit the while-loop)
  while head:

    # we need to keep track of the node we're currently on
    currentNode = head

    # we need to iterate through the linked list - this makes sure we move to the next node
    head = head.next

    # this is how we manipulate the pointers
    # we "reverse the pointer" here
    currentNode.next = previousNode

    # we build the reversed linked list here
    previousNode = currentNode
  
  # we return the head of the reversed linked list 
  # (which was formally the last node of the original lsit)
  return previousNode



'''
input = 1 -> 2 -> 3 -> 4

output = 1 <- 2 <- 3 <- 4

---------------------------

prevNode = None

1st iteration:

while (1):
  curr = 1 (head)

  head = head.next (2)

  curr.next = None (prev)

  prev = 1 (curr)

---------------------------
2nd iteration:

while (2):
  curr = 2

  head = 3 (head.next)

  curr.next = 1 (prev)

  prev = 2

---------------------------
3rd iteration:

while (3):
  curr = 3

  head = 4 (head.next)

  curr.next = prev

  prev = 4

---------------------------
4th iteration

while (4):
  curr = 4

  head = None (head.next)

  curr.next = 3 (prev)

  prev = 4

---------------------------
5th iteration

while (None) = False

return 4
'''
def reverseList(head):
  if not head:
    return None
  
  newHead = head
  
  if head.next:
    newHead = reverseList(head.next)
  
    head.next.next = head
  
  head.next = None
  
  return newHead
