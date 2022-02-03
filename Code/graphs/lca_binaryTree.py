'''
LeetCode #236

For Lowest Common Ancestors we have 3 scenarios:

1. 1 of the given nodes is in the left subtree and 1 of the given nodes is in the right subtree
  - In which case the the LCA is a root/parents node

2. Both p and q are in the left subtree, but one of them is the root node and the other is the child (return whichever is the root)
3. Both p and q are in the right subtree, but one of them is the root node and the other is the child (return whichever is the root)

We don't have a BST to direct our traversal, so we will search the tree completely till we find p and q
We will do a Post Order Traversal
'''

# recursive solution
def lowestCommonAncestor(self, root, p, q):
  """
  :type root: TreeNode
  :type p: TreeNode
  :type q: TreeNode
  :rtype: TreeNode
  """
  # If looking for me, return myself
  if root == p or root == q:
    return root
  
  left = right = None
  
  # else look in left and right child
  if root.left:
    left = self.lowestCommonAncestor(root.left, p, q)
  if root.right:
    right = self.lowestCommonAncestor(root.right, p, q)

  # if both children returned a node, means
  # both p and q found so parent is LCA
  if left and right:
    return root

  else:
  # either one of the chidren returned a node, meaning either p or q found on left or right branch.
  # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
  # somewhere below node where 'p' was found we dont need to search all the way, 
  # because in such scenarios, node where 'p' found is LCA
    return left or right

'''
lowest common ancestor

Time Complexity: O(n)
Space Complexity: O(n)
'''

'''
iterative solution
'''
def lowestCommonAncestor(root, p, q):
  stack = [root]
  parent = {root: None}
  while p not in parent or q not in parent:
    node = stack.pop()
    if node.left:
      parent[node.left] = node
      stack.append(node.left)
    if node.right:
      parent[node.right] = node
      stack.append(node.right)
  ancestors = set()
  while p:
    ancestors.add(p)
    p = parent[p]
  while q not in ancestors:
    q = parent[q]
  return q
