class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
The naive solution here is a straightforward recursive one:

If the current node is between the lower and upper range, then return the current node's value plus (recursively) the sum of the values in the range of the left child plus the right child.
If it's not in the range, then we just recursively return the sum of the values in the range of the children.
'''
def sum_range(node, lower, upper):
  if node is None:
    return 0

  return sum_range(node.left, lower, upper) + sum_range(node.right, lower, upper) + (node.val if lower <= node.val <= upper else 0)

# Time Complexity: O(n) - we must check all nodes in the tree

'''
BUT we don't need to check EVERY node

For example, if the current node we're looking at is smaller than the lower bound,
              * then there is no need to keep on recursively checking left since they're all smaller (by the property of the BST).
              * Similar logic applies to the upper bound. Thus we can speed up our algorithm by doing the following:

1. If the current node's value is between lower and upper:
    - Return the sum_range of the left child plus the right child plus the current node's value

2. If the current node's value is outside lower and upper:
    - Then either it's lower or higher. 
        - If it's lower, then we only need to check the right child (since we know that everything left of it will be smaller.
        - And if it's higher, then we only need to check the left child.
'''
def sum_range_fast(node, lower, upper):
  if node is None:
    return 0

  if lower <= node.val <= upper:
    return sum_range_fast(node.left, lower, upper) + sum_range_fast(node.right, lower, upper) + node.val

  if node.left < lower:
    return sum_range_fast(node.right, lower, upper)

  if node.right > upper:
    return sum_range_fast(node.left, lower, upper)

# This still takes O(n) time, but it is faster since we skip all unnecessary checks.
