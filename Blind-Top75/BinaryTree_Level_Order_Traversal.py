'''
LeetCode #102 - Level Order Traversal

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

Since we need to traverse all nodes of each level before moving onto the next level,

We can use the Breadth First Search (BFS) technique to solve this problem.

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
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def bfs(root):
  # result will hold a sublists
  # each sublist will hold nodes of the same level
  result = []
  
  # queue will hold all the nodes we have to traverse
  # when the queue is empty that means we're done traversing the tree
  queue = deque()
  queue.append(root)

  while queue:
    # levelSize will limit how many nodes we iterate for the currentLevel
    # this is how we carryout the level order traversal
    levelSize = len(queue)
    # currentLevel will add every node we see on the current level - which we then append to result
    currentLevel = []

    for _ in range(levelSize):
      # identify the node we're on
      currentNode = queue.popleft()
      # append the currentNode to currentlevel
      currentLevel.append(currentNode.val)

      # if the currentNode has a left child add it to the queue
      if currentNode.left:
        queue.append(currentNode.left)
        
      # if the currentNode has a right child add it to the queue
      if currentNode.right:
        queue.append(currentNode.right)
    
    # when we're done traversing the currentLevel
    # we append the currentlevel list to result
    result.append(currentLevel)
  
  # when we finish traversing the tree - we return result
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
