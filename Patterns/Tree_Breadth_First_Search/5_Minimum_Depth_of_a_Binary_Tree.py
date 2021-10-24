'''
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

        12
      /     \
    7        1
  /         / \
 9        10   5
        /
      11
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def minimumDepth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  depth = 0

  while queue:
    levelSize = len(queue)
    depth += 1
    
    for _ in range(levelSize):
      currentNode = queue.popleft()

      if currentNode.left is None and currentNode.right is None:
        return depth

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  print("Tree Minimum Depth: " + str(minimumDepth(root)))

  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)

  print("Tree Minimum Depth: " + str(minimumDepth(root)))

main()

'''
Time Complexity: O(n) -> where 'n' is the total number of nodes in the tree
Space Complexity: O(n) -> With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''
