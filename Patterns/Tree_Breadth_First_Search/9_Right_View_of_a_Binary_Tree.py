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

Right View: [12, 1, 5, 20]
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def tree_right_view(root):
  result = []
  
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)

  while queue:
    levelSize = len(queue)

    for i in range(levelSize):
      currentNode = queue.popleft()
      
      # if the currentNode is the LAST node on this level -> Append it
      # last nodes on every level are the nodes on the right-side of the Binary Tree
      if i == levelSize-1:
        result.append(currentNode)
      
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
  
  return result


def rightSideView(root):
  def collect(node, depth):
    if node:
        # same idea -> we keep traversing the tree, till we hit the last element in our current tree level
        # and then append it to view
        if depth == len(res):
          res.append(node.val)
        collect(node.right, depth+1)
        collect(node.left, depth+1)
        
  res = []
  collect(root, 0)
  return res

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.left.left = TreeNode(9)
  root.left.left.left = TreeNode(3)

  root.right.left = TreeNode(10)
  root.right.left.right = TreeNode(20)
  root.right.right = TreeNode(5)
  print("Recursive Solution: ", rightSideView(root))

  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')

main()

'''
Time Complexity: O(N) - where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space Complexity: O(N) - With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue

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
    #   i = 0 range(0,4) CN = 4

    #   i = 2 range(0,2) CN = 3
    #   i = 1 range(0,2) CN = 2

    #   i = 0 range(0,1) CN = 1
    for i in range(levelSize):
      currentNode = queue.popleft()      # 1             # 2             # 3             # 4             # 5
      
      # 3 == 3 (CN=7)
      # 2 == 3 (CN=6)
      # 1 == 3 (CN=5)
      # 0 == 3 (CN=4)

      # 1 == 1 (CN=3)
      # 0 == 1 (CN=2)

      # 0 == 0 (CN=1)
      if i == levelSize-1:
        # [1,3] -> [1,3,7] (CN=7)
        # [1] -> [1,3] (CN=3)
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
