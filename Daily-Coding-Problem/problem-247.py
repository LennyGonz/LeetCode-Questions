def helper(root):
  if root is None:
    return 0

  left = helper(root.left)
  if left == -1:
    return -1

  right = helper(root.right)
  
  if right == -1:
    return -1

  if abs(left - right) > 1:
    return -1

  return max(left, right) + 1

def is_balanced(root):
  return helper(root) != -1

'''
Our helper function generates two subproblems at each node of size N / 2, but the time required to combine these subproblems is only O(1)
As we are only taking their maximum. Again by the master theorem, we can express the time complexity as T(N) = 2 * T(N / 2) + O(1), which resolves to O(N).
'''
