class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def create_sides(points):
  sides = [(points[-1], points[0])] + list(zip(points, points[1:]))
  return [(Point(*a), Point(*b)) for (a, b) in sides]

def intersects(p, side):
  p1, p2 = side

  # Get the slope and intercept of the side. Check for zero and undefined slopes.
  dy, dx = (p2.y - p1.y), (p2.x - p1.x)
  if dx == 0.0:
    return 1 if p.x < p1.x and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y) else 0
  if dy == 0.0:
    return 0

  slope = dy / dx
  intercept = p1.y - slope * p1.x

  # Plug in the y-coordinate of our point and solve for the intersection.
  intersection = Point((p.y - intercept) / slope, p.y)

  # Check to see if the intersection is valid before returning.
  if p.x <= intersection.x and min(p1.y, p2.y) <= intersection.y <= max(p1.y, p2.y):
    return 1
  else:
    return 0

def check_inside(p, polygon):
  p = Point(*p)

  count = 0
  sides = create_sides(polygon)
  for side in sides:
    count += intersects(p, side)

  if count % 2 == 1:
    return True
  else:
    return False
