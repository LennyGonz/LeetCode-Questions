from __future__ import print_function
from collections import deque

'''
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

ex 1:
            12
          /     \
        7         1
      /         /   \
    9          10    5
  /               \
3                 20

Left View: [12, 7, 9, 3]
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def tree_left_view(root):
  result = []

  if root is None:
    return result
  
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)

    for i in range(levelSize):
      currentNode = queue.popleft()

      if i == 0:
        result.append(currentNode)
      
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
  
  return result

'''
Walk-Through

def tree_right_view(root):
  result = []
  
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)
    #   i = 3 range(0,4) CN = 7
    #   i = 2 range(0,4) CN = 6
    #   i = 1 range(0,4) CN = 5
    #   i = 0 range(0,4) CN = 4 *

    #   i = 1 range(0,2) CN = 3
    #   i = 0 range(0,2) CN = 2 *

    #   i = 0 range(0,1) CN = 1 *
    for i in range(levelSize):
      currentNode = queue.popleft()
      
      # 3 == 0 (CN=7)
      # 2 == 0 (CN=6)
      # 1 == 0 (CN=5)
      # 0 == 0 (CN=4) *

      # 1 == 0 (CN=3)
      # 0 == 0 (CN=2) *

      # 0 == 0 (CN=1) *
      if i == 0:
        # [1,2] -> [1,2,4] (CN=4)
        # [1] -> [1,2] (CN=2)
        # [] -> [1] (CN=1)
        result.append(currentNode)
      
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
  
  # r: 1     # r: 2       # r: 3         # r: 4       # r: 5     # r: 6   # r: 7
  # Q: [2,3] # Q: [3,4,5] # Q: [4,5,6,7] # Q: [5,6,7] # Q: [6,7] # Q: [7] # Q: [] -> exit while-loop
  return result
'''

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.left.left = TreeNode(9)
  root.left.left.left = TreeNode(3)

  root.right.left = TreeNode(10)
  root.right.left.right = TreeNode(20)
  root.right.right = TreeNode(5)

  result = tree_left_view(root)
  print("Tree left view: ")
  for node in result:
    print(str(node.val) + " ", end='')

main()
