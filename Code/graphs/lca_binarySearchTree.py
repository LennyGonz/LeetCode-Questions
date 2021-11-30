class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def lowestCommonAncestorBinarySearchTree(root, p ,q):
  curr = root
  
  while curr:
    if p.val > curr.val and q.val > curr.val:
      curr = curr.right

    elif p.val < curr.val and q.val < curr.val:
      curr = curr.left
    
    else:
      return curr.val

def main():
  root = TreeNode(6)
  
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(4)
  
  root.right.left = TreeNode(7)
  root.right.right = TreeNode(9)
  
  root.left.right.left = TreeNode(3)
  root.left.right.right = TreeNode(5)
  
  p = TreeNode(2)
  q = TreeNode(8)
  
  n1 = TreeNode(2)
  n2 = TreeNode(4)
  print("The Lowest Common Ancestor is:", lowestCommonAncestorBinarySearchTree(root, p, q), " - p:2 & q:8")
  print("The Lowest Common Ancestor is:",lowestCommonAncestorBinarySearchTree(root, n1, n2)," - p:2 & q:4")

main()
