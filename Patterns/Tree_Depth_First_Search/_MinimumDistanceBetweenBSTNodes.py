'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree

Input: root = [4,2,6,1,3]
        4
      /   \
     2     6
    / \
   1   3
Output: 1
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  pre = float("-inf")
  res = float("inf")

  def minDiffInBST(self, root):
    if root.left:
      self.minDiffInBST(root.left)
    
    self.res = min(self.res, root.val - self.pre)
    self.pre = root.val

    if root.right:
      self.minDiffInBST(root.right)
    
    return self.res

