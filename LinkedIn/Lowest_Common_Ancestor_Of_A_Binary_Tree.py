'''
For Lowest Common Ancestors we have 3 scenarios:

1. 1 of the given nodes is in the left subtree and 1 of the given nodes is in the right subtree
  - In which case the the LCA is a root/parents node

2. Both p and q are in the left subtree, but one of them is the root node and the other is the child (return whichever is the root)
3. Both p and q are in the right subtree, but one of them is the root node and the other is the child (return whichever is the root)

We don't have a BST to direct our traversal, so we will search the tree completely till we find p and q
We will do a Post Order Traversal
'''
class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def lowestCommonAncestor(root, p, q):
  # while traversing if the currentNode is p or q
  # it means we've located the node, so we return it
  if root == p or root == q:
    return root
  
  # we will use these variables to search the left and right subtree
  left = right = None
  
  # recursively search the left subtree
  if root.left:
    left = lowestCommonAncestor(root.left, p, q)
  
  # recursively search the right subtree
  if root.right:
    right = lowestCommonAncestor(root.right, p, q)
  
  # we if recursively search the left and right subtree
  # and only found 1 of 2 - we have scenario #2 or #3
  else:
    return left or right
  
'''
Time: O(N) - we traverse all the nodes
Space: O(N) - the call stack holds n recursive calls
'''
