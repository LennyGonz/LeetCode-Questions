def get_points(intervals):
  intervals.sort(key=lambda x: (x[1], x[0]))

  points = []
  latest_endpoint = None

  for start, end in intervals:
    if start <= latest_endpoint:
      continue
    else:
      points.append(end)
      latest_endpoint = end

  return points
