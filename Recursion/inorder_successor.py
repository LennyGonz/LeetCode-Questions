class Solution:
  previous, inorderSuccessorNode = None, None

  def inorderSuccessor(self, root, givenNode):
    if givenNode.right:
      leftmost = givenNode.right

      while leftmost.left:
        leftmost = leftmost.left
      
      self.inorderSuccessorNode = leftmost
    
    else:
      self.inorderTraversal(root, givenNode)
  
  def inorderTraversal(self, root, givenNode):
    if not root:
      return
    
    self.inorderTraversal(root.left, givenNode)

    if self.previous == givenNode and not self.inorderSuccessorNode:
      self.inorderSuccessorNode = root
      return
      
    self.previous = root

    self.inorderTraversal(root.right, givenNode)
