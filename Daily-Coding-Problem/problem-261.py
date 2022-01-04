# First note that regardless of how we build the tree, we would like each leaf node to represent a character.
class Node:
  def __init__(self, char, left=None, right=None):
    self.char = char
    self.left = left
    self.right = right

'''
When building the tree, we should try to ensure that less frequent characters end up further away from the root. We can accomplish this as follows:

Start by initializing one node for each letter.
Create a new node whose children are the two least common letters, and whose value is the sum of their frequencies.
Continuing in this way, take each node, in order of increasing letter frequency, and combine it with another node.
When the there is a path from the root to each character, stop.

For example, suppose our letter frequencies were {'a': 3, 'c': 6, 'e': 8, 'f': 2}.

The stages to create our tree would be as follows:

  (5)
 /   \
f     a

      (11)
     /    \  
  (5)      c
 /   \
f     a

            (19)
          /     \
      (11)       e
     /    \
  (5)      c
 /   \
f     a

'''

import heapq

def build_tree(frequencies):
  nodes = []
  for char, frequency in frequencies.items():
    heapq.heappush(nodes, (frequency, Node(char)))

  while len(nodes) > 1:
    f1, n1 = heapq.heappop(nodes)
    f2, n2 = heapq.heappop(nodes)
    node = Node('*', left=n1, right=n2)
    heapq.heappush(nodes, (f1 + f2, node))

  root = nodes[0][1]

  return root

# Each pop and push operation takes O(log N) time, so building this tree will be O(N * log N), where N is the number of characters.

def encode(root, string="", mapping={}):
  if not root:
    return

  if not root.left and not root.right:
    mapping[root.char] = string

  encode(root.left, string + "0", mapping)
  encode(root.right, string + "1", mapping)

  return mapping

# It will take, on average, O(log N) time to traverse the path to any character, so encoding a string of length M using this tree will take O(M log N)
