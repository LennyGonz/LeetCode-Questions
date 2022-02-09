'''
LeetCode #314 - Binary Tree Vertical Order Traversal - Facebook & Bloomberg & Amazon & Microsoft & Apple & Salesforce & Google & Snapchat

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Check the README file in this folder
'''

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
  def verticalOrder(self, root):
    columnTable = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
      node, column = queue.popleft()

      if node is not None:
        columnTable[column].append(node.val)
        
        queue.append((node.left, column - 1))
        queue.append((node.right, column + 1))

    return [columnTable[x] for x in sorted(columnTable.keys())]

# BFS w/o sorting

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
  def verticalOrder(self, root):
    if root is None:
      return []

    columnTable = defaultdict(list)
    min_column = max_column = 0
    queue = deque([(root, 0)])

    while queue:
      node, column = queue.popleft()

      if node is not None:
        columnTable[column].append(node.val)
        min_column = min(min_column, column)
        max_column = max(max_column, column)

        queue.append((node.left, column - 1))
        queue.append((node.right, column + 1))

    return [columnTable[x] for x in range(min_column, max_column + 1)]

'''
Complexity Analysis

Time Complexity: O(N) where N is the number of nodes in the tree.
Following the same analysis in the previous BFS approach, the only difference is that this time we don't need the costy sorting operation (i.e. O(NlogN)).

Space Complexity: O(N) where N is the number of nodes in the tree. The analysis follows the same logic as in the previous BFS approach.
'''

# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
  def verticalOrder(self, root):
    if root is None:
      return []

    columnTable = defaultdict(list)
    min_column = max_column = 0

    def DFS(node, row, column):
      if node is not None:
        nonlocal min_column, max_column
        columnTable[column].append((row, node.val))
        min_column = min(min_column, column)
        max_column = max(max_column, column)

        # preorder DFS
        DFS(node.left, row + 1, column - 1)
        DFS(node.right, row + 1, column + 1)

    DFS(root, 0, 0)

    # order by column and sort by row
    ret = []
    for col in range(min_column, max_column + 1):
      columnTable[col].sort(key=lambda x:x[0])
      colVals = [val for row, val in columnTable[col]]
      ret.append(colVals)

    return ret
