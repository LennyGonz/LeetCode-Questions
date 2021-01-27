'''
Time Complexity: O(n)
Space Complexity: O(n)

    2
   / \
  1   3 // valid tree!

    5
   / \
  1   4  // not valid here!
     / \
    3   6
'''

def isValidBST(self, root):
  return check_bst(root, float("-inf"), float("inf"))

def check_bst(self, node, left, right):
  if not node:
    return True
  
  if not left < node.val < right:
    return False
  
  return (check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right))
