from __future__ import print_function
from collections import deque

'''
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node

ex1:
        1 ->
      /   \
    2  ->  3 ->
  /   \   /  \
4 -> 5 ->6 -> 7 ->
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None, next=None):
    self.val = val
    self.left = None
    self.right = None
    self.next = None
  
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " -> ", end="")

        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
      
        current = current.next
      print()

def connect_level_order_siblings(root):
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)
    previousNode = None

    for _ in range(levelSize):
      currentNode = queue.popleft()

      if previousNode:
        previousNode.next = currentNode
      previousNode = currentNode

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

'''
Time Complexity : O(N) - where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space Complexity: O(N) - With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.left.left = TreeNode(9)

  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  connect_level_order_siblings(root)
  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()

main()
