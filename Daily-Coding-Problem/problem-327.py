'''
As with many tree-based coding problems, we can solve this recursively.

There are a few base cases we must handle when combining nodes:
  - If neither tree has a node in a particular spot, we should return a leaf node of None.
  - If only one of the trees has a node somewhere, the merged node should simply be a copy of the node.

For example, suppose we are combining the following trees:

    1      10
   / \       \
  2   3       30
 /
5

For the merged tree, any node that exists in the subtree beginning at 2 in the first tree should be copied over to the result, since there are no corresponding elements to add from the second tree.

Otherwise, we are left with the case of overlapping nodes.

Here, we can create a new node whose value is the sum of the values of its component nodes.

The left and right children of this node will then be recursively constructed.
'''
class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def merge(t1, t2):
  if not t1 and not t2:
    return None

  elif not t1:
    return t2

  elif not t2:
    return t1

  else:
    node = Node(t1.data + t2.data)
    node.left = merge(t1.left, t2.left)
    node.right = merge(t1.right, t2.right)
    return node

'''
Alternatively, we can solve this iteratively, by taking nodes from the second tree and combining them one at a time with the first tree.

We will implement this using a stack that stores tuples for corresponding subtrees, starting with the roots.

For each pair we pop, we first check if the both nodes have associated values. If so, we add the value in the second tree's node to that of the first.

If there is no left child for the first tree, we set it to be the second tree's left child.

Otherwise, we add to our stack a tuple for both left subtrees. We then follow the same process for the right children.

When we finally exhaust the stack, all the second tree's nodes will either be added to existing nodes, or substituted for empty nodes, in the first tree.

Finally, we return our first tree.
'''
def merge(t1, t2):
  stack = [(t1, t2)]

  if not t1:
    return t2

  while stack:
    n1, n2 = stack.pop()

    if not n1 or not n2:
      continue

    n1.data += n2.data

    if not n1.left:
      n1.left = n2.left
    else:
      stack.append((n1.left, n2.left))

    if not n1.right:
      n1.right = n2.right
    else:
      stack.append((n1.right, n2.right))

  return t1
'''
Both of these algorithms will run in O(M + N) time and space, where M is the number of nodes in the first tree and N is the number of nodes in the second.
This is because it takes linear time to traverse each tree, and we must construct a merged tree with at most M + N elements.
'''
