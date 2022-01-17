'''
PostOrder is : root leftChild rightChild
InOrder is : leftChild root rightChild

With postOrder the 3rd value of the list will be the root
However, the main root, is the last node visited so we traverse the postOrder traversal in reverse

Same strategy as PreOrder and Inorder just different implementation

InOrder tells us which subtree the nodes belong in
PostOrder will tell us the root - when traversed in reverse, the root will be the last/first element depending on how you look at it
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# inOrder and postOrder are lists of TreeNodes
def buildTree(inorder, postorder):
  if not postorder or not inorder:
    return None
  
  root = TreeNode(postorder[-1])
  mid = inorder.index(postorder[-1])
  
  root.left = buildTree(inorder[:mid], postorder[:mid])
  root.right = buildTree(inorder[mid+1:], postorder[mid:-1])
  
  return root

'''
Time: O(N)
Space: O(N) - the recursive calls on the call stack
'''
