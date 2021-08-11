from Queue import Queue
from collections import defaultdict

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def minimum_level_sum(root):
  queue = Queue()
  queue.put((root, 0))
  level_to_sum = defaultdict(int) # Maps level to its sum


  while not queue.empty():
    node, level = queue.get()
    level_to_sum[level] += node.val

    if node.right:
      queue.put((node.right, level + 1))

    if node.left:
      queue.put((node.left, level + 1))

  return min(level_to_sum, key=level_to_sum.get)
