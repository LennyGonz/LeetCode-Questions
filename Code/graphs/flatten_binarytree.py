class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def flatten(root):
  currentNode = root

  while currentNode:
    print("currentNode: ", currentNode.val)
    if currentNode != None:
      pNode = currentNode.left

      while pNode.right != None:
        pNode = pNode.right
        #print("pNode: ",pNode.val)
      
      pNode.right = currentNode.right

      currentNode.right = currentNode.left

      currentNode.left = None
    
    #print("CN.val: ",currentNode.val)
    currentNode = currentNode.right

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(5)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(4)
  root.right.right = TreeNode(6)

  print(flatten(root))

main()
