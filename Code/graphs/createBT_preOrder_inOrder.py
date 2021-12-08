class TreeNode:
  def __inite__(self, val=0,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right
    
  
def buildTree(preorder,inorder):
  if preorder is None or inorder is None:
    return None
  
  root = TreeNode(preorder[0])
  mid = inorder.Index(preorder[0])
  
  root.left = buildTree(preorder[1,mid+1],inorder[:mid])
  root.right = buildTree(preorder[mid+1:],inorder[mid+1:])
  
  return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder,inorder))

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
