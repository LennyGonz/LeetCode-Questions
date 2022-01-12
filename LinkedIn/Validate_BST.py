'''
A valid BST is:

1. The left subtree of a node contains only nodes with values LESS THAN the current node's value
2. The right substree of a node contains only nodes with values GREATER than the current node's value
3. Both the left and right subtree must also be BSTs

so the strategy is

we need to traverse every level of the tree and make sure that these conditions are true

(rightNode.val > currentNode.val) and (leftNode.val < currentNode.val)

We need to do this on every level and for every parent node, because we need to make sure that 
every left subtree and right subtree is also a valid BST

SO

As we traverse each node we test the node for both of these conditions, if it fails either test, we immediately return False

So when we traverse the left subtree: -infinity < currentNode.val < root.val
root.val is the right bound
-infinity is the left bound

when traversing the right subtree: root.val < currentNode.val < infinity
infinity is the right bound
root.val is the left bound
'''

def isValid(root):
  def valid(node, left, right):
    if not node:
      return True
    
    # by doing it this way, we skip nodes that follow BST rules
    # and catch nodes that violate the rules
    if not (node.val < right and node.val > left):
      return False

    return (valid(node.left,left,node.val) and valid(node.right, node.val, right))
  
  return valid(root, float("-inf"), float("inf"))
