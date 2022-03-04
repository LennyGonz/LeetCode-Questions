class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
LeetCode #114

Every linked list has a head node and in this case, we also need the tail node.
Once recursion does the hard work for us and flattens out the subtrees, we will essentially get two linked lists and we need the tail end of the left one to attach it to the right one.
Let's see what all information we will need in our recursive function at a given node.

The linked list should be in the same order as a preorder traversal of the binary tree
so we dont have to worry about the root, but then we just do a recursive definition
- visit the root
- then left subtree
- then right subtree

1. For a given node, we will recursively flatten out the left and the right subtrees 
    and store their corresponding tail nodes in leftTail and rightTail respectively.

2. Next, we will make the following connections (only if there is a left child for the current node, else the leftTail would be null)
    - leftTail.right = node.right
    - node.right = node.left
    - node.left = None

3. Next we have to return the tail of the final, flattened out tree rooted at node. 
    - So, if the node has a right child, then we will return the rightTail, else, we'll return the leftTail.
    
All of this is done in place - dont return anything
Time: O(N)
Space: O(N)
'''

def flatten(root):
  def flattenTree(node):
    if node is not None:
      return None

    if node.left is None and node.right is None:
      return node
    
    leftTail = flattenTree(node.left)
    rightTail = flattenTree(node.right)
    
    if leftTail:
      leftTail.right = node.right
      node.right = node.left
      node.left = None
    
    return rightTail if rightTail else leftTail


    

# in place solution Time: O(N) - Space: O(1)
def flatten(root):
  currentNode = root

  while currentNode:

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
