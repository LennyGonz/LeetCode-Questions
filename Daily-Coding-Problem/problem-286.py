import heapq

def create_skyline(buildings):
  buildings += [(r, r, 0) for (_, r, _) in buildings]
  buildings.sort(key=lambda x: (x[0], -x[2]))

  skyline = []
  heap = [(0, float("inf"))]

  for left, right, height in buildings:
    while heap and left >= heap[0][1]: 
      heapq.heappop(heap)

    heapq.heappush(heap, (-height, right))

    if not skyline or skyline[-1][1] != -heap[0][0]: 
      skyline.append((left, -heap[0][0]))

  return skyline

'''
After adding these zero-length points, the list of buildings will contain 2N elements, which will take O(N log N) time to sort.

For each element in the list, we perform one push operation, and possibly several pop operations. 

However, since in total the number of elements that can be popped from or pushed to the heap is 2N, there will be O(N) operations which each take O(log N) time, for an overall time complexity of O(N log N).

Both the heap and solution array can have no more than 2N elements, so the space required will be O(N).
'''
