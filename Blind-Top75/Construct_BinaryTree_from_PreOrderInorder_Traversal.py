'''
LeetCode #105

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PreOrder is : root leftChild rightChild
InOrder is : leftChild root rightChild

So the first value in the preOrder list will always be the root, then the leftChild, then the rightChild
  - so we have the first 3 nodes, but for the subsequent nodes we don't know 
  - which is the leftChild and which is the rightChild for each parent node

This is where the inOrder array comes in handy

We use the inOrder array to distinguish which nodes belong in the left subtree and right subtree

ex) PreOrder = [3,9,20,15,7] and InOrder = [9,3,15,20,7]

IO = [9,3,15,20,7] -> our root is 3, we use preorder to determine that
Notice how every value to the left of 3 is going to the left subtree 
AND
every value to the right of 3 is going to the right subtree

Once we're done building the left subtree
We move onto the right subtree

InOrder = [15,20,7]  if not head:
      return None
  
  newHead = head
  
  if head.next:
      newHead = self.reverseList(head.next)
  
      head.next.next = head
  
  head.next = None
  
  return newHead
We move to the middle element 20, because using the PreOrder traversal, we can determine that's the root of the right subtree
to the left of 20 is 15 (leftChild)
to the right of 20 is 7 (rightChild)
'''

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
inorder = [9,3,15,20,7]'''
LeetCode #105

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PreOrder is : root leftChild rightChild
InOrder is : leftChild root rightChild

So the first value in the preOrder list will always be the root, then the leftChild, then the rightChild
  - so we have the first 3 nodes, but for the subsequent nodes we don't know 
  - which is the leftChild and which is the rightChild for each parent node

This is where the inOrder array comes in handy

We use the inOrder array to distinguish which nodes belong in the left subtree and right subtree

ex) PreOrder = [3,9,20,15,7] and InOrder = [9,3,15,20,7]

IO = [9,3,15,20,7] -> our root is 3, we use preorder to determine that
Notice how every value to the left of 3 is going to the left subtree 
AND
every value to the right of 3 is going to the right subtree

Once we're done building the left subtree
We move onto the right subtree

InOrder = [15,20,7]  if not head:
      return None
  
  newHead = head
  
  if head.next:
      newHead = self.reverseList(head.next)
  
      head.next.next = head
  
  head.next = None
  
  return newHead
We move to the middle element 20, because using the PreOrder traversal, we can determine that's the root of the right subtree
to the left of 20 is 15 (leftChild)
to the right of 20 is 7 (rightChild)
'''

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
