class TreeNode:
  def __init__(self, val=None, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def postorderTraversal(root):
  res = []
  helper(root, res)
  print(res)

def helper(root, res):
  if root:
    helper(root.left, res)
    helper(root.right, res)
    res.append(root.val)

if __name__ == '__main__':
  """ Construct the following tree
              1
            /   \
          /     \
          2       3
        /      /   \
        /      /     \
      4      5       6
            / \
            /   \
          7     8
  """

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  postorderTraversal(root)

def postOrder(root):
  stack = [root]
  res = []

  while stack:
    curr = stack.pop()
    res.append(curr.val)

    if curr.left:
      stack.append(curr.left)
    
    if curr.right:
      stack.append(curr.right)

  # print postorder traversal
  return [element for element in reversed(res)]

if __name__ == '__main__':
  '''
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  '''
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  print(postOrder(root))
