import math

# Assume points are already sorted by x-coordinate
def closest_pair(points):
  def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

  def closest_pair_brute_force(points):
    min_pair, min_dist = None, float('inf')

    for p1 in points:
      for p2 in points:
        if p1 is p2:
          continue
        dist = distance(p1, p2)
        if dist < min_dist:
          min_pair = (p1, p2)
          min_dist = dist

    return min_pair, min_dist

  def find_cross_pair(points, x_boundary, min_dist):
    cross_points = []
    # Discard points not within min_dist from the boundary
    for p in points:
      if abs(p[0] - x_boundary) < min_dist:
        cross_points.append(p)

    # Sort the points by y-coordinate.
    # To achieve better time complexity, we want to sort once
    # at the beginning, and keep the ordering while we divide
    # and recurse. This involves extra book-keeping.
    cross_points.sort(key=lambda x: x[1])

    min_pair, min_dist = None, float('inf')
    # For each point in the sorted points, check the distance
    # with all subsequent points the distance in y reaches min_dist.
    # This is shown to be no greater than 7 pairs per point.
    for i, p1 in enumerate(cross_points):
      for p2 in cross_points[i + 1:]:
        if p2[1] - p1[1] >= min_dist:
          break
        dist = distance(p1, p2)
        if dist < min_dist:
          min_pair = (p1, p2)
          min_dist = dist

    return min_pair, min_dist

  size = len(points)
  if size <= 3:  # Base case
    return closest_pair_brute_force(points)

  left = points[:size//2]
  right = points[size//2:]

  # Recursively call function on left and right halves
  closest_pair_left, dist_left = closest_pair(left)
  closest_pair_right, dist_right = closest_pair(right)
  print(closest_pair_left, closest_pair_right)

  # Next, we need to find the minimum-distance pair of points that crosses
  min_dist = min(dist_left, dist_right)
  x_boundary = right[0][0] # Get the dividing x-boundary between the halves
  closest_pair_cross, dist_cross = find_cross_pair(points, x_boundary, min_dist)

  min_tup = min((closest_pair_left, dist_left),
                (closest_pair_right, dist_right),
                (closest_pair_cross, dist_cross),
                key=lambda tup: tup[1])
  return min_tup
