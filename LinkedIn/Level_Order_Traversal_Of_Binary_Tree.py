'''
LeetCode #102 - Level Order Traversal

Since we need to traverse all nodes of each level before moving onto the next level,

we can use the Breadth First Search (BFS) technique to solve this problem.

We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (let's call it levelSize). We will have these many nodes in the current level.
4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.
'''

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  # result list will hold sublists, each sublist represents nodes at each level
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  
  while queue:
    # we use levelSize as our range to correctly traverse the # of number nodes at the current level
    levelSize = len(queue)
    # this will hold all the nodes at the currentLevel
    currentLevel = []
    
    for _ in range(levelSize):
      # identify the node we're currently on at the current level  
      currentNode = queue.popleft()
      
      # add the node to the current level
      currentLevel.append(currentNode.val)
      
      # insert the children of current node in the queue
      # these children are the nodes, we'll be traversing in the next iteration
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    # append the sublist of nodes of the level we were just on
    result.append(currentLevel)

  # return the list of lists
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
