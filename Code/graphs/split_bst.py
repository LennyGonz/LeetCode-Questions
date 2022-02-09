'''
LeetCode #776 Split BST

Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees

- where one subtree has nodes that are all smaller or equal to the target value,
- while the other subtree has all nodes that are greater than the target value.

It Is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain.
Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees.

Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,null,null,5,7]]

Strategy:

The root node either belongs to the first half or the second half. Let's say it belongs to the first half.

Then, because the given tree is a binary search tree (BST), the entire subtree at root.left must be in the first half.
However, the subtree at root.right may have nodes in either halves, so it needs to be split.

In the diagram above, the thick lines represent the main child relationships between the nodes, while the thinner colored lines represent the subtrees after the split.

Lets say our secondary answer bns = split(root.right) is the result of such a split.
Recall that bns[0] and bns[1] will both be BSTs on either side of the split.
The left half of bns must be in the first half, and it must be to the right of root for the first half to remain a BST.
The right half of bns is the right half in the final answer.
'''

def splitBST(self, root, V):
  if not root:
    return None, None

  elif root.val <= V:
    bns = self.splitBST(root.right, V)
    root.right = bns[0]
    return root, bns[1]

  else:
    bns = self.splitBST(root.left, V)
    root.left = bns[1]
    return bns[0], root

'''
Time: O(N) - where N is the number of nodes in the input tree, as each node is checked once.
Space: O(N) - At worst case we make N recursive calls - so N space on the call stack
'''
