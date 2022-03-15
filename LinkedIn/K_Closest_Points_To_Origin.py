'''
LeetCode #973

The Euclidean distance of a point P(x,y) from the origin can be calculated through the following formula:

√{x^2 + y^2}

This problem follows the Top K Numbers pattern. 
The only difference in this problem is that we need to find the closest point (to the origin) as compared to finding the largest numbers.

We can use a Max Heap to find K points closest to the origin.

While iterating through all points, IF a point (say P) is closer to the origin than the TOP POINT of the max-heap

we will remove that top point from the heap and add P to always keep the closest points in the heap.
'''

from heapq import *

def squared_distance(point):
  """Calculate and return the squared Euclidean distance."""
  return point[0] ** 2 + point[1] ** 2

# LeetCode Response
def kClosest(points, k):
  # heaps are sorted in an increasing order, so I negate the distance to simulate a max heap
  # and fill the heap with the first k elements of points
  heap = [(-squared_distance(points[i]), i) for i in range(k)]

  heapify(heap)

  # then we iterate over the rest of the pairs of points
  # if we find a pair closer to the origin, we replace the root of the heap
  for i in range(k, len(points)):
    dist = -squared_distance(points[i])
    if dist > heap[0][0]:
      # If this point is closer than the kth farthest,
      # discard the farthest point and add this one
      heapreplace(heap, (dist, i))
  
  # Return all points stored in the max heap, because the heap is populated with the k-closest points to the origin
  return [points[i] for (_, i) in heap]

print(kClosest([[1, 3], [3, 4], [2, -1]], 2))

'''
Time: O(N * logK) - Adding to/removing from the heap only takes O(logK) time when the size of the heap is capped at K elements

Space: O(K) - The heap will contain at most k elements
'''

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()
  
  def distance_from_origin(self):
    return (self.x * self.x) + (self.y * self.y)

  def print_point(self):
    print("[", str(self.x) + ", " + str(self.y) + "], ")

def find_closest_points(points, k):
  maxHeap = []
  
  # insert the first k points into our heap
  for i in range(k):
    heappush(maxHeap, points[i])

  # iterate over the rest of the input array and replace the maxHeap root if we find a set of points with a smaller distance
  for i in range(k, len(points)):
    if (points[i].distance_from_origin() < maxHeap[0].distance_from_origin()):
      heappop(maxHeap)
      heappush(maxHeap, points[i])
  
  return list(maxHeap)

def main():
  result = find_closest_points([Point(1,3), Point(3,4), Point(2,-1), Point(1,2), Point(2,3), Point(1,4), Point(4,5)], 3)
  print("Here are the k points closest to the origin: ")
  
  for point in result:
    point.print_point()

main()
'''
Time: O(N logK) - we traverse over the entire input array (N) * worst case we have to pop&push every pair into the heap
Space: O(K) - our heap has K nodes at all times
'''
