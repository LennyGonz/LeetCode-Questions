import heapq

def k_sort(array, k):
  res = []

  heap = []
  for i in range(k):
    heapq.heappush(heap, array[i])

  for i in range(k, len(array)):
    heapq.heappush(heap, array[i])
    res.append(heapq.heappop(heap))

  while heap:
    res.append(heapq.heappop(heap))

  return res

'''
Since each heap push and pop operation is O(log K), and we will perform each of these N times.
This algorithm will satisfy our time requirement of O(N log k).

The space complexity will be O(N), since we must build up a new result of all the elements.
'''
