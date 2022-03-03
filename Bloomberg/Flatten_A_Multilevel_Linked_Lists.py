'''
Leetcode #430

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list.
Let curr be a node with a child list.
The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] *3 has a child node of 7->8->9->10 & 8 has a child node of 11->12
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

------------------------------------------------------------------------------------------------------------------------------------------------

This problem is pretty weird, and figuring out how to tackle it can be hard

So it's best we approach this LIKE a graph

We want to traverse the linked list as deep as possible
Before we traverse the neighbor nodes -> we want to visit the child node first

So to keep track of the current nodes neighbor and its child, we use a stack...

But the general algorithm should look like this:

1) Put head of the list at the top of the stack (so we can start traversing)
  - we pop the element from the stack *this is what starts it
  - add the nodes 2 other properities(next and child) to our auxiliary stack, which we'll call order
    - the order of visiting is important, we want to visit the CHILD FIRST, THEN the neighbor

2) Each time we pop the last element from the stack, we append the node to our order-stack
3) Last step is to rebuild the linked list into a flattened linked list

* so our stack will help us traverse the multilevel linked list and help us visit the children nodes first THEN the neighbors
  * we use the auxilary stack (order) - to keep track of the flattened order of the linked list that we'll need to rebuild and eventually return
'''


# Definition for a MultiLevel-Doubly-LinkedList Node.
class Node:
  def __init__(self, val, prev, next, child):
    self.val = val
    self.prev = prev
    self.next = next
    self.child = child

def flatten(self, head):
  # base case - given an empty list
  if not head:
    return head
  
  # we'll use the stack to help us traverse the multi-level linked list
  # in the order of children then neighbor
  stack = [head]
  
  # this list will help us connect the flattened linked list
  order = []

  while stack:
    # last will hold the current node we're on
    last = stack.pop()
    
    # we're traversing in the correct order, so we append the current node we're on
    order.append(last)
    
    # if the current node has a neighbor we append it first BC it'll be behind a potential child of the current node
    if last.next:
      stack.append(last.next)
    
    # if the current node has a child, it will be at the top of the stack, and we want to visit the child first
    if last.child:
      stack.append(last.child)
  
  # once we exit the while loop - it means we've finished traversing the multi-level linked list
  # and now we just need to make sure the pointers are correct AND
  # that none of the nodes have a child value
  
  # we iterate through all the nodes in the order list
  # we stop at the 2nd to last node, because we'll connect everything 
  for i in range(len(order) - 1):
    # we make the 2nd node point to the node before it (previous)
    order[i+1].prev = order[i]
    # we make the current node point to the next node (next)
    order[i].next = order[i+1]
    # we make sure the current node has a null value for child
    order[i].child = None

  # once we exit the for loop all the nodes are doubly linked and we can return the head
  return order[0]

'''
Complexity: 

time complexity is O(n), where n is number of nodes in our list.
space complexity is O(n), because I keep order list.

This can be avoid, if we make connections on the fly, but it is a bit less intuitive in my opinion, but ofcourse more optimal in space complexity.

def flatten(self, head):
  if not head: return head
  
  dummy = Node(0)
  
  curr, stack = dummy, [head]
  
  while stack:
  
      last = stack.pop() 
      
      if last.next:
        stack.append(last.next)

      if last.child:
        stack.append(last.child)

      curr.next = last
      last.prev = curr  
      last.child = None
      curr = last
  
  res = dummy.next
  res.prev = None
  return res
  
Time: O(n)
Space: O(1)
'''
