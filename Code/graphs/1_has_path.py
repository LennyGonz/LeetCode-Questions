'''
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.


        1   (false)                                       root.left will return  false || false || True
      /   \
    2      3    sum = 3 + 1 (false) 
  /   \   /   \
  4   5   6    7 sum = 3+1+6 (true) , sum = 1+3+7 (false)

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return False

  # if the current node is a leaf and its value is equal to the sum, we've found a path
  if root.val == sum and root.left is None and root.right is None:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))

main()
'''

def is_path_sum(root, S)->True:
  if root is None:
    return False

  if root.val == S and root.left is None and root.right is None:
    return True
  
  return is_path_sum(root.left, sum-root.val) or is_path_sum(root.right, sum-root.val)


# DFS with stack
def hasPathSum2(self, root, sum):
  if not root:
    return False
  stack = [(root, root.val)]
  while stack:
    curr, val = stack.pop()
    if not curr.left and not curr.right and val == sum:
      return True
    if curr.right:
      stack.append((curr.right, val+curr.right.val))
    if curr.left:
      stack.append((curr.left, val+curr.left.val))
  return False
