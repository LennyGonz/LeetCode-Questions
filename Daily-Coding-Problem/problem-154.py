from time import time

class Stack:
  def __init__(self):
    self.max_heap = MaxHeap()

  def push(self, item):
    t = time()
    self.max_heap.push(item, t)

  def pop(self):
    item, _ = self.max_heap.pop()
    return item


import heapq

class MaxHeap:
  def __init__(self):
    self._heap = []

  def push(self, item, priority):
    heapq.heappush(self._heap, (-priority, item))

  def pop(self):
    _, item = heapq.heappop(self._heap)
    return item
