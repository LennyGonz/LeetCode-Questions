'''
This problem follows the Binary Tree Level Order Traversal pattern.

We can follow the same BFS approach.

The only additional step we have to keep in mind is to alternate the level order traversal,

which means that for every other level, we will traverse similar to Reverse Level Order Traversal.

to do this we use a boolean flag, to trigger the reverse level order traversal

we flip the boolean value at the end of every level traversal
'''

from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def traverse(root):
  # If the input is an empty tree - Added b/c without it this solution fails
  if not root: 
    return []

  result = []

  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    levelSize = len(queue)
    
    # we make currentLevel a queue INSTEAD OF A LIST
    # SO we can appendLeft when leftToRight is False
    # creating the zigzag effect
    currentLevel = deque()

    for _ in range(levelSize):
      currentNode = queue.popleft() # 1 # 2 -> 3 # 4 -> 5 -> 6 -> 7

      if leftToRight: # True # - # True 
        currentLevel.append(currentNode.val) # [1] # - # [4] -> [4,5] -> [4,5,6] -> [4,5,6,7]
      
      # appendLEFT - when leftToRight is False
      else: # - # False # -
        currentLevel.appendleft(currentNode.val) # - # [2] -> [3,2]

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left) # [2] # [3,4] -> [4,5,6] # [5,6,7] -> [6,7] -> [7] -> 7
      if currentNode.right:
        queue.append(currentNode.right) # [2,3] # [3,4,5] -> [4,5,6,7] # [5,6,7] -> [6,7] -> [7] -> []

    result.append(list(currentLevel)) # [[1]] # [[1],[3,2]] # [[1],[3,2],[4,5,6,7]]
    
    # we finished traversing the current level, so we flip the boolean value
    leftToRight = not leftToRight # not True -> False # not False -> True # not True -> False

  return result # [[1],[3,2],[4,5,6,7]]

'''
Time: O(N) - where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) - B/c as we need to return a list containing the level order traversal. We will also need O(N) space for the queue.
              Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
              therefore we will need O(N) space to store them in the queue.
'''
