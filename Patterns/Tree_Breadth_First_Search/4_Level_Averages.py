'''
Given a binary tree, populate an array to represent the averages of all of its levels.

        1
      /   \
    2      3
  /   \   /  \
 4     5 6    7

Level Averages: [1.0, 2.5, 5.5]
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def levelAverages(root):
  result = []
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)
    levelSum = 0.0

    for _ in range(levelSize):
      currentNode = queue.popleft()
      levelSum += currentNode.val

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    
    result.append(levelSum/levelSize)
  
  return result

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  print("Level Averages in Binary Tree: ", levelAverages(root))

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
