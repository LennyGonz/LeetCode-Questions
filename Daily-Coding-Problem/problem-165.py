import bisect

def smaller_counts(lst):
  result = []
  s = []
  for num in reversed(lst):
    i = bisect.bisect_left(s, num)
    result.append(i)
    bisect.insort(s, num)
  return list(reversed(result))
