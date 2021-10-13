'''
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. There will be two differences:

  - Every time we find a root-to-leaf path, we will store it in a list.
  - We will traverse all paths and will not stop processing after finding the first path.

        12
      /    \
     7      1
   /       /  \
  4       10   5

'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  allPaths = []
  find_paths_recursive(root, required_sum, [], allPaths)
  return allPaths


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
  if currentNode is None:
    return

  # add the current node to the path
  currentPath.append(currentNode.val)

  # if the current node is a leaf and its value is equal to required_sum, save the current path
  if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  else:
    # traverse the left sub-tree
    find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
    # traverse the right sub-tree
    find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()

'''
The time complexity of the above algorithm is O(N^2), where ‘N’ is the total number of nodes in the tree. 

This is due to the fact that we traverse each node once (which will take O(N)), and for every leaf node, we might have to store its path (by making a copy of the current path) which will take O(N).

We can calculate a tighter time complexity of O(NlogN) from the space complexity discussion below


If we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(N) in the worst case.

This space will be used to store the recursion stack. The worst-case will happen when the given tree is a linked list (i.e., every node has only one child).
'''

def allPaths(root):
  allPaths = []
  helper(root, [], allPaths)
  return allPaths

def helper(currentNode, currentPath, allPaths):
  if currentNode is None:
    return
  
  currentPath.append(currentNode.val)

  if currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  
  else:
    helper(currentNode.left, currentPath, allPaths)
    helper(currentNode.right, currentPath, allPaths)

  del currentPath[-1]

def main2():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum: " + str(allPaths(root)))


main2()

def maxSum(root):
  maxsum = 0
  result = []
  helper2(root, [], maxsum, result)
  return max(result)

def helper2(currentNode, currentPath, maximumSum, res):
  if currentNode is None:
    return

  currentPath.append(currentNode.val)

  if currentNode.left is None and currentNode.right is None:
    #print("CP: ", currentPath)
    maximumSum = max(maximumSum, sum(currentPath))
    res.append(maximumSum)
    #print("ms: ", maximumSum)
  
  else:
    helper2(currentNode.left, currentPath, maximumSum, res)
    helper2(currentNode.right, currentPath, maximumSum, res)
  
  currentPath.pop()

def main3():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(5)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Max Sum: " + str(maxSum(root)))

main3()
