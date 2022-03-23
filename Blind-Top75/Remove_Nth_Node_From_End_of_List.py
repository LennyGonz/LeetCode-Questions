'''
Leetcode #19

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

-----------------------------------------------------------------------------------------------------------

The challenge is identifying the nth node from the end of the list...
My idea is to use 2 pointers: start and end

* we initialize start to be at the first node
* we initialize end to be at the nth node

    1 -> 2 -> 3 -> 4 -> 5 -> None
    ^         ^
    |         |
1   Start     End (starting at the Nth node) 
         ^         ^
         |         |
2        Start     End
              ^          ^
              |          |
3             Start      End
                    ^         ^
                    |         |
4                   Start     End

Notice that on the 4th iteration, when the end pointer reaches the end of the linked list (None)
  the start pointer is pointing at the nth node from the end!
  
  BUT we need the start pointer to stop at node BEFORE the nth node, so that we can connect node 3 to node 5
    -> to accomodate this we use a dummy node

Instead of initializing the start pointer at the head of the linked list, we initialize it to our dummy node
  * the end pointer needs to stay at the nth node

So we traverse the array using both nodes
  when the end pinter reach the end of the linked list
    start will be at the n-1 node
      At this node we can change its next pointer to skip over the nth node from the end

At the end we can simply do "return DummyNode.next"

Time: O(N) - We traverse the linked list 1 time, where N is the total number of nodes in the list
Space: O(1) - algorithm runs in constant space
'''
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeNthFromEnd(head, n):
  # this dummy node will be where we place the start pointer
  # we need to start here so when end reaches the end of the linked list
  # the start pointer lands on the n-1th node
  dummy = ListNode(0, head)
  
  # place our pointers
  start = dummy
  end = head 

  # we want our end pointer to start N nodes from head, so we start iterating the linked list in order to place our end pointer where we want it
  # so when it reached the end of the list -> start pointer is where want it to be
  while n > 0 and end:
    end = end.next
    n -= 1
  
  # we start traversing the linked list till end reaches the end of the linked list
  # leaving the start pointer at the node before the nth node from the end
  while end:
    start = start.next
    end = end.next
  
  # here we give the Nth-1 node from the end a new node to point at
  # essentially removing the Nth node
  start.next = start.next.next
  
  # since we made dummy.next point to head, we can just return this
  return dummy.next
