'''
Given the root of a Binary Search Tree and a target number: k, return True
If there exists two elements in the BST such that their sum is equal to the given target

          5
        /   \
       3     6
     /   \     \
    2     4     7

Input: root = [5,3,6,2,4,null,7]
k = 9
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def findTarget(root, k):
    if root.left is None and root.right is None:
      return False
    
    def inOrder(root,res):
      if not root:
        return
      
      inOrder(root.left, res)
      res.append(root.val)
      inOrder(root.right, res)
    
    res = []
    dic = {}

    for num in res:
      if dic.get(k-num):
        return True
      
      dic[num] = True
    
    return False
