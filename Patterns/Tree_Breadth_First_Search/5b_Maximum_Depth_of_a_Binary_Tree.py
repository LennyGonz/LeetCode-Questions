'''
Given a binary tree, find its maximum depth (or height)

        12
      /     \
    7        1
  /         / \
 9        10   5
        /
      11

Similar to Minimum Depth of a Binary Tree, instead of returning as soon as we find a leaf node, we will keep traversing for all the levels, incrementing treeHeight each time we complete a level.
'''
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maximumDepth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  treeHeight = 0

  while queue:
    levelSize = len(queue)
    treeHeight += 1

    for _ in range(levelSize):
      currentNode = queue.popleft()

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
  
  return treeHeight

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  print("Tree Maxiumum Depth: " + str(maximumDepth(root)))

  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)

  print("Tree Maxiumum Depth: " + str(maximumDepth(root)))

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
