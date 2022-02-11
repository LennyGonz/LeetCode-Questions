'''
LeetCode #1644 - LCA BT II - Facebook & Microsoft & Amazon & LinkedIn

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q.
If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

----------------------------------------------------------------------------------------------------------------

Key Things to be aware about the find LCA II:

1.  Two target nodes is not guaranteed to exist in the tree
2.  A node is considered as descendant of itself.
So remember that:

we cannot instantly return the node we found here because we don't know if all m and n exist in the tree!
'''
# Approach 1 
'''
Basically the exact same solution as LC 236-Lowest Common Ancestor of a Binary Tree, except we need to keep track of whether both p and q exist in the tree. If both of them are, return node. Otherwise, return null.

Time Complexity:
O(n), n = number of nodes in the tree

Typical DFS algorithms has O(V+E) time complexity, where V stands for vertices and E stands for edges. According to the definition of tree, we have N-1 number of edges. Therefore the time complexity resolves to O(N+N-1) = O(2N-1) ~ O(N)
Space Complexity
O(n) -- recursion stack space + return values

# Six possible valid answers:
"""
1. 
   parent
 /         \
p           q


2. 
   parent
 /         \
q           p

3.
  p
   \
	q
	
4.
  q
   \
	p

5.
     q
   /
 p
	
6.
      p
   / 
 q
"""
# found[0] = true -- means p is found.
# found[1] = true -- means q is found
'''
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node, found):
      if not node: return None
      l, r = dfs(node.left, found), dfs(node.right, found)
      if node == p or node == q:
        if node == p:
          found[0] = True
        else:
          found[1] = True
        return node
      if l and r:
        return node
      return l or r
    found = [False, False]
    ans = dfs(root, found)
    return ans if found[0] and found[1] else None

# Approach 2 - Breadth First Search
'''
The idea is simmilar with 1257, first visit all the nodes and record their parents, then use a set to store all the parents of one node and traverse the next node's ancestors to find the first parent in the set.

Complexity: O(n) in space, O(n) in time
'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  parents = {root.val:None}
  stack = [root]
  while stack:
    node = stack.pop(0)
    if node.left:
      parents[node.left.val] = node
      stack.append(node.left)
    if node.right:
      parents[node.right.val] = node
      stack.append(node.right)
  ancestors = set()
  if p.val not in parents or q.val not in parents: return None
  while p:
      ancestors.add(p.val)
      p = parents[p.val]
  while q and q.val not in ancestors:
      q = parents[q.val]
  return q

# Approach 3
'''
Depth First Search
The idea is simmilar with 236. First call l, r to finish the traversal of a tree and used self.countp， self.countq to check the two target nodes exsit in the tree.
Complexity: O(n) in space, O(n) in time
'''

def dfs(self, root, p, q):
  if not root: return None
  l = self.dfs(root.left, p, q)
  r = self.dfs(root.right, p, q)
  if root.val == p.val: 
      self.countp += 1
      return root
  if root.val == q.val: 
      self.countq += 1
      return root
  if l and r: return root
  return l or r

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  self.countp = 0
  self.countq = 0
  ans = self.dfs(root, p, q)
  if not self.countp or not self.countq: return None
  return ans  

# Approach 4
class Solution:
  def dfs(self, curr, p, q):
    if not curr:
      return None, False
    
    l, fl = self.dfs(curr.left, p, q)
    r, fr = self.dfs(curr.right, p, q)

		# Block 1
    if l and r:
      # Find LCA
      return curr, True

		# Block 2
    if curr == p or curr == q:
      # Find a matching node, the 2nd element in the tuple indicates whether this is a LCA
      return curr, l or r

    # Block 3
    # Simply propagating the result if nothing interested happens
    return (l, fl) if l else (r, fr)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      a, b = self.dfs(root, p, q)
      
      if not b:
        return None
      
      return a
