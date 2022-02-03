'''
LeetCode #106

PostOrder is : root leftChild rightChild
InOrder is : leftChild root rightChild

With postOrder the 3rd value of the list will be the root
However, the main root, is the last node visited (so the very last node in the preOrder list is the main root)
so we traverse the postOrder array in reverse

Same strategy as PreOrder and Inorder just different implementation

InOrder tells us which subtree the nodes belong in
PostOrder will tell us the root - when traverse in reverse, the root will be the last/first element depending on how you look at it

root = TreeNode(PostOrder[-1])

WE use a variable we'll call "mid" to distinguish the left & right subtree
Every element in Inorder from 0 to mid-1 belongs in the left subtree
Every element in Order from mid+1 to len(n) belongs in the right subtree

ex) PostOrder = [9,1,2,12,7,5,3,11,4,8] & InOrder = [9,5,1,7,2,12,8,4,3,11]
The last element in PostOrder is the main root -> root = PostOrder[-1]
Then we identify the position of that root in InOrder -> mid = InOrder.index(root)

Then as we recursively call builTree 
to build the left subtree we pass: InOrder[:mid] & PostOrder[:mid] 
to build the right subtree we pass: InOrder[mid+1:] & PostOrder[mid:-1] *we do -1 b/c we want to skip the last element (which we identified to be the root) 

example:

PostOrder = [9,1,2,12,7,5,3,11,4,8]
InOrder = [9,5,1,7,2,12,8,4,3,11]

root = 8
mid = InOrder.index(root) # mid = 6

InOrder = [9,5,1,7,2,12,8,4,3,11]
           0 1 2 3 4  5 6 7 8  9
          |            |^|      |
          these nodes  mid  these nodes belong in the right subtree
          in the left
          subtree

* Remember InOrder tell us which substree the nodes belong in
* when traverse PostOrder in reverse, the root will be the last/first element (depending on how you look at it)

So after we take the identify the main root in PostOrder - we don't even iterate over that element, we skip it and focus on the rest
Then, every 3rd element will be a root

PostOrder = [9,1,2,12,7,5,3,11,4,8] & InOrder = [9,5,1,7,2,12,8,4,3,11]
Since mid = 6


8.left = InOrder[:mid] & PostOrder[:mid]    - 8.right = InOrder[mid+1:] & PostOrder[mid:-1]
root.left = [9,5,1,7,2,12] & [9,1,2,12,7,5] - root.right = [4,3,11] & [3,11,4]
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
  
  # identify the root - which will be the last node of the postorder list
  root = TreeNode(postorder[-1])
  
  # find the index of where the root is in the inorder list
  mid = inorder.index(postorder[-1])
  
  # all nodes to the left of mid belong in the left subtree
  root.left = buildTree(inorder[:mid], postorder[:mid])
  
  # all nodes to the right of mid belong in the right subtree
  root.right = buildTree(inorder[mid+1:], postorder[mid:-1])
  
  return root

'''
Time: O(N) -> we traverse N nodes in the tree
Space: O(N) -> we make N recursive calls so our call stack has N recursive calls
'''

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
