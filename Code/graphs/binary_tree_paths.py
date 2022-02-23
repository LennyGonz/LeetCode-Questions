class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
LeetCode #257 - Binary Tree Paths - Easy

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

    1
  /   \
 2     3
  \
   5

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
------------------------------------------------------------------------------

So the strategy is to traverse every path in the tree using DFS

When we start traversing WE ALSO begin with an empty string

The empty string will track the entire path from root to leaf

The first node we encounter will be the root node 
  -> We check if there even is a root node 
    -> if there is a valid root node we continue with the algorithm 
    -> else return

  -> If we have a valid root, and the root has children
    -> We stringify the integer value of the root
      -> concatenate the empty string(path) WITH the value of the root node AND an arrow "->"
        -> ex) "1 ->"
  -> Then we do a recursive call going down the left most path and we repeat the process
  -> IF we reach a leaf node
    -> then we append the last node to our string: path
    -> append the current path to our result list: res
    -> and return to the top most recursive call

We repeat this process until we've traveresed the entire tree
'''

def binaryTreePathsHelper(self, root, res, path):
  # if we reach a node that is None - we just return out of the recursive call
  if root:
    return
  
  # if we reached a leaf node
  # we append it to the path 
  # append the path to the result list
  # return to the top-level recursive call
  if root.left is None and root.right is None:
    path += str(root.val)
    
    res.append(path)
    
    return

  # IF the currentNode is not a leaf node - we traverse down the left most path
  # passing along our result list
  # AND most importantly we must update our path with each recursive call - so we concatentate our path string with the current node and an arrow
  self.binaryTreePathsHelper(root.left, res, path + str(root.val)+"->")
  self.binaryTreePathsHelper(root.right, res, path + str(root.val)+"->")

  # once we've traversed the entire tree we can exit the helper function
  return

def binaryTreePaths(self,root):
  # if we're given a None node, we can immediately return
  if root is None:
    return
  
  # our result list that will hold all the paths
  res = []
  
  # invoke our helper function
  # we pass in the root node - our result list - and an empty string that will record each path we traverse
  self.binaryTreePathsHelper(root, res, "")
  
  # res will hold all the paths in the tree at the end of the recursive call so we return our result list
  return res

'''
Time: O(N) - we traverse the entire tree, where N is the number of nodes in the given tree
Space: O(N) - the recursive calls on the call stack
'''

def main():
  root = Node(1)

  root.left = Node(2)
  root.right = Node(3)
  
  root.left.right = Node(5)

  print(binaryTreePaths(root))

main()
