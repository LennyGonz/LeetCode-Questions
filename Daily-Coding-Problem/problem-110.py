'''
We conveniently store the parent node for the path function, so we can find the ancestors to get their path to the root. We can initialize our binary tree with this code:


    For the binary tree shown below:

      1
     / \
    2   3
       / \
      4   5

root = Node(
  value=1,
  left=Node(2),
  right=Node(3, Node(4), Node(5))
)
'''

class BSTNode:
  def __init__(self, value, left=None, right=None):
    self.parent = None
    self.value = value
    self.left = left
    self.right = right
    if left:
      left.parent = self
    if right:
      right.parent = self

  def path(self):
    path = []
    current = self
    while current:
      path = [current.value] + path
      current = current.parent
    return path

  def find_leaves(node):
    leaves = []
    queue = list()
    queue.append(node)
    while len(queue):
      node = queue.pop()
      if not node.left and not node.right:
        leaves += [node.path()]
        continue
      if node.right:
        queue.append(node.right)
      if node.left:
        queue.append(node.left)
    return leaves
