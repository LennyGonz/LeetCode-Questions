def intersects(l1, l2):
    # these lines intersect iff l1[0] > l2[0] and l1[1] > l2[1] or vice versa
  return (l1[0] < l2[0] and l1[1] > l2[1]) or (l1[0] > l2[0] and l1[1] < l2[1])


def num_intersections(lst1, lst2):
  line_segments = list(zip(lst1, lst2))
  count = 0
  for i, l1 in enumerate(line_segments):
    for l2 in line_segments[i + 1:]:
      if intersects(l1, l2):
        count += 1
  return count
