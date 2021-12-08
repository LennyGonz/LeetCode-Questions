'''
LeetCode #106 
Time: O(N) -> we traverse N nodes in the tree
Space: O(N) -> we make N recursive calls so our call stack has N recursive calls
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def buildTree(inorder, postOrder):
  if not inorder or not postOrder:
    return None
  
  root = TreeNode(postOrder[-1])
  mid = inorder.index(postOrder[-1])
  
  root.left = buildTree(inorder[:mid], inorder[:mid])
  root.right = buildTree(inorder[mid+1:], postOrder[mid:-1])

  return root

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  '''
  Need to figure out how to make the lists into nodes so we can build the BT
  '''
  print("BFS Level Order Traversal: ", buildTree(root))

main()
