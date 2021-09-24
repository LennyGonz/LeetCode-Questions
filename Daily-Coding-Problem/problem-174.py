class Shape:
  def draw(self, coords):
    print("Drawing shape at", coords)

class Circle(Shape):
  def draw(self, coords):
    print("Drawing circle at", coords)

class Square(Shape):
  def draw(self, coords):
    print("Drawing square at", coords)

def render_scene(objs, coords):
  for shape, coord in zip(objs, coords):
    shape.draw(coord)
