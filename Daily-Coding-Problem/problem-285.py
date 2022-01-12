def sunset_views(buildings):
  views = []
  highest = 0

  for building in buildings:
    while views and views[-1] <= building:
      views.pop()
    views.append(building)

  return len(views)

'''
At first it may seem that the time complexity of this algorithm should be greater than that of our first solution, because of the inner while loop.
However, note that, at most, we can only pop and append N elements, so in fact this will run in O(N) time as well.
In this case, though, we must use O(N) space to store the buildings in our stack.
'''
