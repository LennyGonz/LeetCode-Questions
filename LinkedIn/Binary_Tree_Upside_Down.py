'''
Given the root of a binary tree, turn the tree upside down and return the new root

1. the original left child becomes the new root
2. the original root becomes the new right child
3. the original right child becomes the new left child

Strategy:

Since we're turning every level upside down
We need to start at the bottom!
We traverse the tree to the leftmost leaf node
Once we find the leaf nodes, we simply start redefining the left and right pointer values
HOWEVER, from a recursive approach we start flipping pointer values using the parent node of whatever child node we're on,
we do this as to not get confused with which node is supposed to point to which node
'''
class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def upsideDownBinaryTree(root):
  def dfs(currentNode):
    # if there is no longer a left node to traverse, return the currentNode
    if not currentNode.left:
      return currentNode
    
    # our new root is the left most node in the input tree
    newRoot = dfs(currentNode.left)
    
    currentNode.left.left = currentNode.right
    currentNode.left.right = currentNode
    
    currentNode.left = None
    currentNode.right = None
    
    return newRoot
  
  return dfs(root) if root else None

'''
Time: O(log(N)) - only traversing the nodes on the left most path
Space: O(log(N)) - we only traverse the nodes on the left most path - recursive calls on the call stack
'''
