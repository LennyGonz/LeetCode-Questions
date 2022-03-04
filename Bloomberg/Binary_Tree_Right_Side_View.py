from collections import deque
'''
LeetCode #199

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom

ex 1:
            12
          /     \
        7         1
      /         /   \
    9          10    5
  /               \
3                 20

Right View: [12, 1, 5, 20]

This can be done very easily using level order traversal

We simply traverse each level and append the last node on the level to a list
'''

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

# recursive solution
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

'''
Time Complexity: O(N) - where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space Complexity: O(N) - With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
