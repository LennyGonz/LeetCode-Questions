from __future__ import print_function
from collections import deque

'''
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

        1 -> (2)
      /   \
    2  ->  3 -> (4)
  /   \   /  \
4 -> 5 ->6 -> 7 -> null
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None, next=None):
    self.val = val
    self.left = None
    self.right = None
    self.next = None
  
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " -> ", end='')
      current = current.next

def connect_all_siblings(root):
  queue = deque()
  queue.append(root)
  previousNode = None
  
  while queue:
    currentNode = queue.popleft()     # 1        # 2      # 3      # 4      # 5      # 6      # 7

    if previousNode:                  # None     # 1      # 2      # 3      # 4      # 5      # 6
      previousNode.next = currentNode # None     # 1 -> 2 # 2 -> 3 # 3 -> 4 # 4 -> 5 # 5 -> 6 # 6 -> 7
    previousNode = currentNode        # 1        # 2      # 3      # 4      # 5      # 6      # 7

    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)
    
    # r: 1     # r: 2       # r: 3         # r: 4       # r: 5     # r: 6   # r: 7
    # Q: [2,3] # Q: [3,4,5] # Q: [4,5,6,7] # Q: [5,6,7] # Q: [6,7] # Q: [7] # Q: [] *exit while-loop*

'''
It's critical to identify whether you need to traverse level by level OR more of a fluid traversal
It's still BFS, but not as systemic

By doing a more fluid BFS traversal, we can connect nodes from the previous level to the current level without having to figure out how to keep the previousNode value

* Remember - when we were connecting level order siblings we needed the systemic BFS traversal, because we were connecting nodes on the same level
* AND by keeping the previousNode value outside the for-loop we could hold the value of the previousNode from the previous iteration
* HOWEVER, once we finish traversing all the nodes on that level, we restart the entire while loop, thus reseting the value of previousNode
* In this instance, that's a problem bc we NEED to remember the value of previousNode after finishing traversing each level

Thus fluid BFS is more optimal in this situation
It's key to identify when you need to:
- traverse systematically with levels
OR
- traverse fluidly


Time Complexity: O(N) - where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space Complexity: O(N) - With the use of the queue, we can have a max of n/2 nodes at any level (this only happens at the lowest level),
                          therefore O(n) space is needed to store them in the queue
'''

def main():
  root = TreeNode(12)

  root.left = TreeNode(7)
  root.right = TreeNode(1)

  root.left.left = TreeNode(9)

  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  connect_all_siblings(root)
  root.print_tree()

main()
