def merge(intervals):
  result = []
  for start, end in sorted(intervals, key=lambda i: i[0]):
    # If current interval overlaps with the previous one, combine them
    if result and start <= result[-1][1]:
      prev_start, prev_end = result[-1]
      result[-1] = (prev_start, max(end, prev_end))
    else:
      result.append((start, end))
  return result
