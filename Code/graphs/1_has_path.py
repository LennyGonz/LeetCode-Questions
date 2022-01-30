'''
LeetCode #112 - Path Sum

Given a binary tree and a number Target, find if the tree has a path from root-to-leaf 
  such that the sum of all the nodes from the value to leaf equal Target

ex: Target = 10 & BT:
        1   (false)                                       root.left will return  false || false || True
      /   \
    2      3    sum = 3 + 1 (false) 
  /   \   /   \
  4   5   6    7 sum = 3+1+6 (true) , sum = 1+3+7 (false)

We recurisvely traverse the tree using dfs.
At every node we make 2 recursive calls:
- 1 recursive call to the left child
- 1 recursive call to the right child

SO

1. Start DFS with the root of the tree.
2. If the current node is NOT a leaf node, do two things:
    - Subtract the value of the current node from the given number to get a new sum => Target = Target - currentNode.value
    - Make two recursive calls for both the children of the currentNode with the new Target calculated in the previous step.

3. At EVERY step, see if the current node being visited is a leaf node and if its value is equal to the given number Target
    - (that's being decreased with every recursive call). 
    - If both these conditions are true, we have found the required root-to-leaf path, therefore return true.

4. If the current node is a leaf but its value is not equal to the given number 'S', return false.

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
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def has_path(root, targetSum):
  # if we reach a left node and call on dfs on its left and right child -> then we don't have a path from root to leaf that equals targetSum
  if root is None:
    # if there's no path we must return False
    return False

  # If we reach leaf node (root.left is None and root.right is None)
  # AND
  # the value of this leaf node == targetSum -> we found a path from root to leaf that equals targetSum
  if root.val == targetSum and root.left is None and root.right is None:
    # since we found a path, we can return True
    return True
  
  # if we have not reached a leaf node yet, we make 2 recursive calls
  # 1 recursive call to the currentNode's left child
  # 1 recursive call to the currentNode's right child
  return has_path(root.left, targetSum-root.val) or has_path(root.right, targetSum-root.val)

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

# DFS with stack
def hasPathSum2(root, targetSum):
  if not root:
    return False
  stack = [(root, root.val)]
  while stack:
    curr, val = stack.pop()
    if not curr.left and not curr.right and val == targetSum:
      return True
    if curr.right:
      stack.append((curr.right, val+curr.right.val))
    if curr.left:
      stack.append((curr.left, val+curr.left.val))
  return False
