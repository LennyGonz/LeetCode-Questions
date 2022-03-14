'''
LeetCode #235

For Lowest Common Ancestors we have 3 scenarios:

1. 1 of the given nodes is in the left subtree and 1 of the given nodes is in the right subtree
  - In which case the the LCA is a root/parents node

2. Both p and q are in the left subtree, but one of them is the root node and the other is the child (return whichever is the root)
3. Both p and q are in the right subtree, but one of them is the root node and the other is the child (return whichever is the root)

Since we have a BST, we can use BST properties to direct our traversal in order to avoid traversing all the nodes in the worst case
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def lowestCommonAncestorBinarySearchTree(root, p, q):
  curr = root
  
  while curr:
    # if the given nodes are greater - we go to the right subtree
    if p.val > curr.val and q.val > curr.val:
      curr = curr.right
    
    # if the given nodes are less - we go to the left subtree
    elif p.val < curr.val and q.val < curr.val:
      curr = curr.left

    # if the split occurs or we found p or q
    else:
      return curr

'''
Time: O(Log(N)) - where N is the number of nodes in the tree - we're not visiting every node so time complexity is the height of the tree
Space: O(1) - our algorithm runs in constant space, not using additional data structures
'''

def main():
  root = TreeNode(6)
  
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(4)
  
  root.right.left = TreeNode(7)
  root.right.right = TreeNode(9)
  
  root.left.right.left = TreeNode(3)
  root.left.right.right = TreeNode(5)
  
  p = TreeNode(2)
  q = TreeNode(8)
  
  n1 = TreeNode(2)
  n2 = TreeNode(4)
  print("The Lowest Common Ancestor is:", lowestCommonAncestorBinarySearchTree(root, p, q), " - p:2 & q:8")
  print("The Lowest Common Ancestor is:",lowestCommonAncestorBinarySearchTree(root, n1, n2)," - p:2 & q:4")

main()
