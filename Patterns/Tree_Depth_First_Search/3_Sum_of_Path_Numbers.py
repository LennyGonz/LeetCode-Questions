'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_path_numbers(root):
  return find_root_to_leaf_path_numbers(root, 0)

def find_root_to_leaf_path_numbers(currentNode, pathSum):
  if currentNode is None:
    return 0
  
  pathSum = 10 * pathSum * currentNode.val

  if currentNode.left is None and currentNode.right is None:
    return pathSum
  
  return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(currentNode, pathSum):
  if currentNode is None:
    return 0

  # calculate the path number of the current node
  pathSum = 10 * pathSum + currentNode.val

  # if the current node is a leaf, return the current path sum
  if currentNode.left is None and currentNode.right is None:
    return pathSum

  # traverse the left and the right sub-tree
  return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
'''

def pathSum(root, sum):
  if not root: return []
  result = []
  stack = [(root, sum, [])]
  while stack:
    curr, val, ls = stack.pop()
    print("ls: ", ls)
    if not curr.left and not curr.right and val == curr.val:
      result.append(ls + [curr.val])

    if curr.left:
      print("here: ", ls + [curr.val])
      stack.append((curr.left, val - curr.val, ls + [curr.val]))
    if curr.right:
      stack.append((curr.right, val - curr.val, ls + [curr.val]))

  return result

#print(pathSum([5,4,8,11,None,13,4,7,2,None,None,5,1], 22))

class Solution(object):
  def pathSum(self, root, sum):
    if not root: return []
    result = []
    stack = [(root, sum, [])]
    while stack:
      curr, val, ls = stack.pop()
      if not curr.left and not curr.right and val == curr.val:
        result.append(ls + [curr.val])

      if curr.left:
        stack.append((curr.left, val - curr.val, ls + [curr.val]))
      if curr.right:
        stack.append((curr.right, val - curr.val, ls + [curr.val]))

      return result

def cousins(root, x, y):
  def helper(currentNode, parent, depth):
    if currentNode is None or len(results) == 2:
      return
    if currentNode.val == x or currentNode.val == y:
      results.append((parent, depth))
    else:
      helper(currentNode.left, currentNode, depth+1)
      helper(currentNode.right, currentNode, depth+1)
  
  results = []

  helper(root, None, 0)

  return results[0][0] != results[1][0] and results [0][1] != results[1][1]

