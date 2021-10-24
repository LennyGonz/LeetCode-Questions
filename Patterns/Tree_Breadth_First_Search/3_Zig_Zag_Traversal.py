'''
Given a binary tree, populate an array to represent its zigzag level order traversal.

You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

        1
      /   \
    2      3
  /   \   /  \
 4     5 6    7

Zig Zag Traversal: [  [1],
                      [3,2],
                      [4,5,6,7]
                    ]
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def zigZagTraversal(root):
  result = []
  queue = deque()
  queue.append(root)
  leftToRight = True

  while queue:
    levelSize = len(queue)
    currentLevel = deque()

    for _ in range(levelSize):
      currentNode = queue.popleft()

      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)
      
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    
    result.append(list(currentLevel))
    leftToRight = not leftToRight

  return result

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  print("Zig Zag Level Order Traversal: ", zigZagTraversal(root))

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
