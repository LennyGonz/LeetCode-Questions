'''
We don't actually remove the leaves from the tree, instead we calculate for height

Height of a node will be the # of layers of child nodes from current node to the ground floor

* if the current node is a parent - height is the maxHeight between the left subtree and right subtree

so the strategy is to simply do DFS - and start calculating height from the bottom up

solution that removes the leaf is at the bottom
'''
class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def findLeaves(root):
  def getHeight(node):
    # our base case is -1, because we hit this base case when find a leaf node and it does a recursive call on its left and right pointers
    # when it returns -1, our height calculation adds 1 - 1 because it needs to account for the current layer, so leaves offset to 0
    # which is correct because leaf nodes have a height of 0 - they have no layers of children between them and the floor
    if not node:
      return -1
    
    height = max(getHeight(node.left), getHeight(node.right)) + 1
    
    # once height is calculated we created a sublist to append nodes with the same height
    if height >= len(result):
      result.append([])
    
    # height acts as both the height and index of the sublist the node corresponds too
    result[height].append(node.val)
    
    return height
  
  result = []
  
  getHeight(root)
  
  return result

'''
Time: O(N) - N is the total number of nodes in the input tree - we traverse every node only once
Space: O(N^2) - result list is a list of lists
'''

def findLeaves(root):
  leaf = []
  res = []
  
  def helper(node):
    # if we find a leaf node add it to the leaf list
    if not node.left and not node.right:
      leaf.append(node.val)
      return -1
    
    # traverse the left substree till I hit a leaf node
    # once i hit the leaf node, cut it off
    if node.left is not None:
      vs = helper(node.left)
      if vs == -1:
        node.left = None
    
    # traverse the right substree till I hit a leaf node
    # once i hit the leaf node, cut it off
    if node.right is not None:
      vs = helper(node.right)
      if vs == -1:
        node.right = None
    
    return 1
  
  while root is not None:
    vs = helper(root)
    res.append(leaf)
    leaf = []
    if vs == -1:
      break
  
  return res

'''
time: O(HlogN)
space: O(N^2) - result list is a list of lists
'''
