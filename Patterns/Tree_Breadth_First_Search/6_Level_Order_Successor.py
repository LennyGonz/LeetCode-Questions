'''
Given a binary tree and a node, find the level order successor of the given node in the tree.

The level order successor is the node that appears right after the given node in the level order traversal.


        12
      /    \
    7        1
  /        /   \
9         10    5

Given Node: 12
Level Order Successor: 7
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def find_successor(root, key):
  if root is None:
    return 
  
  queue = deque()
  queue.append(root)

  while queue:
    currentNode = queue.popleft()

    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)
    
    if currentNode.val == key:
      break
  
  return queue[0] if queue else None


def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.left.left = TreeNode(9)

  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  result = find_successor(root, 12)

  if result:
    print(result.val) # 7

  result = find_successor(root, 9)

  if result:
    print(result.val) # 10

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
