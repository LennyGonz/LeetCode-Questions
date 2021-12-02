# Given a binary tree, return the level of the tree with minimum sum.

'''
       1      (Level 0 = 1)
      / \
     2   3    (Level 1 = 2 + 3) = 5 lookup[level=1] = lookup[level=1] + root.val
    / \  / \
       4   5  (Level 2 = 4 + 5) = 9 --
'''
class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def minimum_level_sum_impl(root, lookup = None, level=0):
    if root is None:
      return
    if lookup.get(level) != None:
      lookup[level] = lookup[level] + root.val
    else:
      lookup[level] = root.val

    minimum_level_sum_impl(root.left, lookup, level + 1)
    minimum_level_sum_impl(root.right, lookup, level + 1)   

def minimum_level_sum(root):
    lookup = {}
    minimum_level_sum_impl(root, lookup, 0)
    print(lookup)
    return None


root = Node(
    val=1,
    left=Node(2),
    right=Node(3, Node(4), Node(5))
)
print(minimum_level_sum(root))

'''
root = TreeNode(1,TreeNode(2),None)
level2 = TreeNode(3)
root.right = level2


print(min_level(root))
'''
