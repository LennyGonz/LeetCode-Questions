'''
Given a binary tree, populate an array to represent its level-by-level traversal.

You should populate the values of all nodes of each level from left to right in separate sub-arrays.

        1
      /   \
    2      3
  /   \   /  \
 4     5 6    7

level order traversal: [  [1],
                          [2,3],
                          [4,5,6,7]
                        ]
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def bfs(root):
  result = []
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)
    currentLevel = []

    for _ in range(levelSize):
      currentNode = queue.popleft()
      currentLevel.append(currentNode.val)

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    
    result.append(currentLevel)
  
  return result

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  print("BFS Level Order Traversal: ", bfs(root))

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
