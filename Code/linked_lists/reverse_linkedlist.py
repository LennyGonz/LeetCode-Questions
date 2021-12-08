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
