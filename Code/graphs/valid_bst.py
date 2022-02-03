'''
LeetCode #98 - Validate A Binary search tree

    2
   / \
  1   3 // valid tree!

A valid BST is:

1. The left subtree of a node contains only nodes with values LESS THAN the current node's value
2. The right substree of a node contains only nodes with values GREATER than the current node's value
3. Both the left and right subtree must also be BSTs

so the strategy is

we need to traverse every level of the tree and make sure that these conditions are true

(rightNode.val > currentNode.val) and (leftNode.val < currentNode.val)

We need to do this on every level and for every parent node, because we need to make sure that 
every left subtree and right subtree is also a valid BST

SO

As we traverse each node we test the node for both of these conditions, if it fails either test, we immediately return False

So when we traverse the left subtree: -infinity < currentNode.val < root.val
root.val is the right bound
-infinity is the left bound

when traversing the right subtree: root.val < currentNode.val < infinity
infinity is the right bound
root.val is the left bound

def isValidBST(self, root):
    return check_bst(root, float("-inf"), float("inf"))

    2 
   / \
  1   3 
	
1 // -inf < 1 < 2, so it's still valid
3 //  2 < 3 < inf, so it's still a valid tree
2 // -inf < 2 < inf, so it's a valid tree!

And what about an invalid tree?

    5 
   / \
  1   4 
	
1 // -inf < 1 < 5, so it's still a valid tree
4 // 5 > 4 < inf, this tree is not a valid binary tree!	

So here's one way we could implement this logic!
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def validateBinarySearchTree(root):
  def validate(currentNode, lowerBound, upperBound):
    if not currentNode:
      return True
    
    if not (currentNode.val > lowerBound and currentNode.val < upperBound):
      return False
    
    return (validate(currentNode.left, lowerBound, currentNode.val) and validate(currentNode.right, currentNode.val, upperBound))
  
  return validate(root, float("-inf"), float("inf"))

'''
-----------------------
Time: O(n)            |
Space: O(n)           |
-----------------------
'''

def main():
  root = TreeNode(2)
  root.left = TreeNode(1)
  root.right = TreeNode(3)

  print(validateBinarySearchTree(root))

main()
