'''
There is a recursive solution to this problem that is relatively straightforward.

First, we search for the smallest element in our sequence, and put that as the root of our tree.
The left child of this node is then constructed from all the elements to the left in the sequence, and 
the right child is constructed from all the elements to the right.
'''
class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def build_tree(seq):
  if not seq:
    return None

  val = min(seq)
  root, i = Node(val), seq.index(val)

  root.left = build_tree(seq[:i])
  root.right = build_tree(seq[i + 1:])

  return root
'''
Since we must scan each subarray to find the minimum element, this will take O(N^2) time, where N is the length of our sequence.
The tree itself will have N nodes, meaning we will require O(N) space.

-------------------------------------------------------------------------------------
There is an even more efficient solution, however, which uses the following algorithm.
-------------------------------------------------------------------------------------

For each new element, we can start by placing it as the right child of the right-most node. (For the first element, we can simply make it the root.)
Then, we scan upwards, parent by parent, until we reach a node whose value is less than that of the new node.
If such a node exists, we set the new node as its right child, and set the previous right child as the new node's left child.

Let us look at an example. Suppose our list is [1, 3, 2], and we have reached the final element. So far our tree should look like this:

1 
 \
  3

Since 2 is less than its parent but greater than the root, we should set 2 to be the right child of the root, and set 3 to be its left child.

1
  \
    2
   /
  3

Otherwise, it may happen that we scan all the way to the top without finding a smaller element.
Since our tree will always maintain the heap property, this means we have found a new minimum.
In this case, we should set the new element as the root, and set the previous root as its left child.

For example, suppose our sequence was in fact [1, 3, 2, 0].

Continuing from the last diagram, we find that 0 should be the new root, and 1 should be placed as its left child.

      0
    /
  /
1
  \
    2
   /
  3
To implement this, we will declare three arrays that maintain the parent, left child, and right child of each value in our sequence.

We will iterate once through our sequence, applying the rules above to set the appropriate values in these arrays for each element.
Then, we recursively create the tree with a helper function.
'''
def helper(root, seq, left, right):
  if root is None:
    return

  node = Node(seq[root])
  node.left = helper(left[root], seq, left, right)
  node.right = helper(right[root], seq, left, right)

  return node

def build_tree(seq):
  n = len(seq)
  parent, left, right = [None] * n, [None] * n, [None] * n

  root = 0
  for i in range(1, n):
    prev = i - 1

    while seq[i] < seq[prev] and prev != root:
      prev = parent[prev]

    if seq[i] < seq[prev]:
      left[i] = root
      parent[root] = i
      root = i

    else:
      if right[prev] is not None:
        parent[right[prev]] = i
        left[i] = right[prev]

      parent[i] = prev
      right[prev] = i

  return helper(root, seq, left, right)

'''
Since we know in advance exactly what the left and right child of each node should be, creating this tree will take an amount of time that is linear in the length of our input.

Furthermore, for the initial part of our algorithm, we only passed over our sequence once to update our array values, so this algorithm will run in O(N) time and space overall.
'''
