'''
LeetCode #160

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5].
From the head of B, it reads as [5,6,1,8,4,5].
There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.
----------------------------------------------------------------------------------------------------------------

BruteForce:
  For each node in list A, traverse over list B and check whether or not the node is present in list B.
  Time complexity: O(NxM).
    For each of the N nodes in list A, we are traversing over each of the nodes in list B.
    In the worst case, we won't find a match, and so will need to do this until reaching the end of list B,
      giving a worst-case time complexity of O(NxM).

  Space complexity: O(1).
    We aren't allocating any additional data structures, so the amount of extra space used does not grow with the size of the input.

Optimal:
  I see this problem similar to detecting a loop...
  
  We can use 2 pointers (but not fast and slow pointers)
  We have 2 lists
  
  First list has 'a' elements before intersection and 'b' elements after intersection.
  
  Second list has 'c' elements before intersection and 'b' elements after intersection, and c > a.

  1. On the first step we will reach end of first list and for the second list we will be c-a elements before end.
  
  2. When we finish traversing the short list, we switch over the to the long list and traverse it and 
      after c-a steps one of the pointers will be in the beginning of short list and 
        another will be c-a steps from the long list.
  
  3. Finally, we move both pointers with speed one and either we will have common element or 
      they both reach the end in the same time and in this case they will have common None element.
  
  * one pointer is essentially measuring the length of the longer list,
  * the other is measuring the length of the shorter list, and then 
      placing the start pointer for the longer list
  * Then both are stepping through the list together

1. Set pointer pA to point at headA.
2. Set pointer pB to point at headB.
3. While pA and pB are not pointing at the same node:
    - If pA is pointing to a null, set pA to point to headB.
    - Else, set pA to point at pA.next.
    
    - If pB is pointing to a null, set pB to point to headA.
    - Else, set pB to point at pB.next.

4. return the value pointed to by pA (or by pB; they're the same now).
'''
# Definition for a MultiLevel-Doubly-LinkedList Node.
class Node:
  def __init__(self, val, prev, next):
    self.val = val
    self.prev = prev
    self.next = next

def getIntersectionNode(headA, headB):
  # initialize our pointers
  currA = headA
  currB = headB
  
  # while theyre not pointing at the same element keep traversing
  while currA != currB:
    currB = headA if currB is None else currB.next
    currA = headB if currA is None else currA.next

  # if they didn't meet, they will hit the end at the same iteration,
  # currA == currB == None, return either one of them is the same = None
  return currA

'''
Time: O(N + M) we traverse both lists twice, so we will make no more than 2n + 2m = O(m+n)
Space: O(1) - algorithm runs in constant space
'''
