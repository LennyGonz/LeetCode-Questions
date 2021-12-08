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
