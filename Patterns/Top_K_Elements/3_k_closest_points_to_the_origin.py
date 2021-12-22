from heapq import *

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
