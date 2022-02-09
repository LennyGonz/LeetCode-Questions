'''
LeetCode #1650. Lowest Common Ancestor of a Binary Tree III - Facebook & Microsoft & Linkedin & Amazon & Google & SalesForce & ByteDance & Spotify & Apple

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

# Definition for a Node.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
'''

'''
Approach 1

The idea is fairly simple (and the same as finding the convergence point of 2 linked lists).
We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively.
Then we follow their parent pointers until they point to the same node.
When either of the pointers points to root, we set it to the other original starting node. For example, when p1 points to root (i.e p1.parent is None), assign q to p1.
'''
class Solution:
  def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    p1, p2 = p, q
    while p1 != p2:
      p1 = p1.parent if p1.parent else q
      p2 = p2.parent if p2.parent else p
    return p1

'''
Approach 2

I wanted to pose an easy-to-understand alternative to most answers here. We first find the depth of each pointer, and then move each pointer to the same level in the tree. Then, we move the pointers up level by level until they meet.

Summary:

Find the depth of each pointer
Move the deeper pointer up until it is at the same level as the other pointer
Move each pointer up level-by-level until they meet
Time Complexity: O(h)
Space Complexity: O(1)

AN image is available in the images folder
'''
class Solution:
  def get_depth(self, p):
  # helper function to find the depth of the pointer in the tree
    depth = 0
    while p:
      p = p.parent
      depth += 1
    return depth
  
  def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
  # find the depth of each pointer
    p_depth = self.get_depth(p)
    q_depth = self.get_depth(q)
  
    # Move the lower pointer up so that they are each at the same level. 
    # For the smaller depth (p_depth < q_depth or q_depth < p_depth), 
    # the loop will be skipped and the pointer will stay at the same depth.
    for _ in range(p_depth - q_depth):
      p = p.parent
    for _ in range(q_depth - p_depth):
      q = q.parent
    
    # Now that they are at the same depth, move them up the tree in parallel until they meet
    while p != q:
      p=p.parent
      q=q.parent
    return p
