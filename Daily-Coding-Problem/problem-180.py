from Queue import Queue
import math

def interleave(stack):
  size = len(stack)
  queue = Queue()
  # Step 1.
  while stack:
    queue.put(stack.pop())
  # Step 2.
  for _ in range(size / 2):
    queue.put(queue.get())
  # Step 3.
  for _ in range(int(math.ceil(size / 2.0))):
    stack.append(queue.get())
  # Step 4.
  for _ in range(size / 2):
    queue.put(stack.pop())
    queue.put(queue.get())
  if stack:
    queue.put(stack.pop())
  # Step 5.
  while not queue.empty():
    stack.append(queue.get())
  return stack
