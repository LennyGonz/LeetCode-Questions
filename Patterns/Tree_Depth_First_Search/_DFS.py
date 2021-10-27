class Node:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

# Iterative function to perform preorder traversal on the tree
def preorderIterative(root):
  if root is None:
    return

  stack = [root]
  path = []

  # start from the root node (set current node to the root node)
  curr = root

  # loop till stack is empty
  while stack:
    # if the current node exists, print it and push its right child to the stack before moving to its left child
    if curr:
      path.append(curr.data)

      if curr.right:
        stack.append(curr.right)

      curr = curr.left
    # if the current node is None, pop a node from the stack set the current node to the popped node
    else:
      curr = stack.pop()
  
  print("Pre-Order: ",path, "& right answer is: 1 2 4 3 5 7 8")

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

  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)

  preorderIterative(root)
###########################################################################################################

###########################################################################################################
def inorderIterative(root):
  stack = []
  path = []
  curr = root

  while curr or stack:

    if curr:
      stack.append(curr)
      curr = curr.left
    
    else:
      curr = stack.pop()
      path.append(curr.data)
      curr = curr.right
  
  return path
  
  print("In-Order: ",path, "& right answer is: 4 2 1 7 5 8 3 6")

if __name__ == '__main__':
  """ Construct the following tree
              1
            /   \
          /      \
         2        3
        /       /   \
       /       /     \
      4       5       6
             / \
            /   \
           7     8
  """
  # root = Node(1)
  # root.left = Node(2)
  # root.right = Node(3)
  # root.left.left = Node(4)
  # root.left.right = Node(5)
  # root.right.left = Node(6)
  # root.right.right = Node(7)

  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)
  inorderIterative(root)
###########################################################################################################

###########################################################################################################
def postOrder(root):
  stack = [root]
  path = []

  while stack:
    curr = stack.pop()
    path.append(curr.data)

    if curr.left:
      stack.append(curr.left)
    
    if curr.right:
      stack.append(curr.right)
  
  return [elem for elem in reversed(path)]

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

  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)

  print("Post-Order: ",postOrder(root), "& right answer: 4 2 7 8 5 6 3 1")
