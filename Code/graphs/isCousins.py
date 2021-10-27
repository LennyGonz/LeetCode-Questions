from collections import deque, defaultdict
'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

ex 1:

'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def isCousins(root, x, y):
  # Concept is to store the level and parent information here while performing BFS and break early once you have both x and y in nodeMap
  q = deque()
  nodeMap = defaultdict()
  #         node, level, parent
  q.append((root, 0, 0))
  
  while q:
    # if during our traversal we have encountered the cousins in question... WE STOP TRAVERSING
    # not necessary to traverse the entire tree if we already have what we need
    if (x in nodeMap) and (y in nodeMap):
      break

    node, level, parent = q.popleft()
    # while traversing we need to populate the nodeMap
    nodeMap[node.val] = [level, parent]

    # traverse the tree
    if node.left:
      q.append((node.left, level+1, node.val))

    if node.right:
      q.append((node.right, level+1, node.val))

  if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][1] != nodeMap[y][1]:
    return True
  return False

'''
Solution:
* the key is to have 3 pieces of information ready throughout the entire traversal (currentNode, level, parent)
* We use a dictionary to store this information, where the currentNode is the key and the value is a list of the currentNodes level and parent
* We use a dictionary b/c it will be easier to lookup x & y - lookup in a dictionary is O(1)
* While we're traversing the tree, we need to populate the nodeMap!
* Therefore, once we pop an element from the queue we simply do -> nodeMap[currentNode.val] = [level, parent]

* We traverse normally -> if currentNode.left then queue.append(currentNode.left, level+1, currentNode.val)
* this tuple holds (next node to visit, increment the level, the parent of the next node to visit, which is the currentNode)
* We traverse normally -> if currentNode.right then queue.append(currentNode.right, level+1, currentNode.val)

* When we finish traversing, we'll have a nodeMap of every node we encountered in the Binary Tree
* To check if we even traversed x we do nodeMap[x] -> this will return a list of it's [level, parent]
* if x was not encountered during our traversal -> a dictionary would normally throw a keyError, but this is why we use a defaultdict() to avoid this
* But if we did nodeMap[x] -> [level, parent] ... we want the level to be equal so we do           nodeMap[x][0] == nodeMap[y][0]
*                                             ... we DONT want the parents to be the same so we do nodeMap[x][1] != nodeMap[y][1]
* if the conditions are met, x and y are cousins
* else they are siblings or not even in the tree

def isCousins(root, x, y):
  # Concept is to store the level and parent information here while performing BFS and break early once you have both x and y in nodeMap
  q = deque()
  nodeMap = collections.defaultdict()
  #         node, level, parent
  q.append((root, 0, 0))
  
  while q:

    if x in nodeMap and y in nodeMap:
      break

    #  7,     2,      3
    #  6,     2,      3
    #  5,     2,      2
    #  4,     2,      2
    #  3,     1,      1
    #  2,     1,      1
    #  1,     0,      0
    node, level, parent = q.popleft()
    
    #nodeMap[7]       = [2, 3]
    #nodeMap[6]       = [2, 3]
    #nodeMap[5]       = [2, 2]
    #nodeMap[4]       = [2, 2]
    #nodeMap[3]       = [1, 1]
    #nodeMap[2]       = [1, 1]
    #nodeMap[1]       = [0, 0]
    nodeMap[node.val] = [level, parent]

    # 7.left = None
    # 6.left = None
    # 5.left = None
    # 4.left = None
    if node.left:
      [(4,2,2),(5,2,2)]         -> [(4,2,2),(5,2,2),(6,2,2)]
      [(3,1,1)]                 -> [(3,1,1),(4,2,2)]
      []                        -> [(2,1,1)]
      q.append((node.left, level+1, node.val))

    # 7.right = None -> queue is empty -> exit while-loop
    # 6.right = None
    # 5.right = None
    # 4.right = None
    if node.right:
      [(4,2,2),(5,2,2),(6,2,2)] -> [(4,2,2),(5,2,2),(6,2,2),(7,2,2)]
      [(3,1,1),(4,2,2)]         -> [(3,1,1),(4,2,2),(5,2,2)]
      []                        -> [(2,1,1), (3,1,1)]
      q.append((node.right, level+1, node.val))

# nodeMap[key][first element in list value]    |     | 
# nodeMap[4]    -> [2,2] & node[5]    -> [2,2] | AND | nodeMap[4]    -> [2,2] & nodeMap[5]    -> [2,2]
# nodeMap[4][0] -> 2     & node[5][0] -> 2     | AND | nodeMap[4][1] -> 2     & nodeMap[5][1] -> 2

# if the levels are the same        and the parents are NOT the same -> return true  else false
  if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][1] != nodeMap[y][1]:
    return True
  return False
'''

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)

  x = 4
  y = 3
  print("Are " + str(x) + " and " + str(y) + " cousins?", isCousins(root, x, y))

main()

def main2():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  x = 4
  y = 7
  print("Are " + str(x) + " and " + str(y) + " cousins?", isCousins(root, x, y))

main2()
