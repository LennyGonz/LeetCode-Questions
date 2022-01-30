def find_broadcast_range(listeners, towers):
  min_range = 0; i = 0
  towers = [-float('inf')] + towers + [float('inf')]

  for listener in listeners:
    while listener > towers[i + 1]:
      i += 1

    curr = min(listener - towers[i], towers[i + 1] - listener)
    min_range = max(min_range, curr)

  return min_rang

# This approach will take O(M + N) time, since we only need to make one pass through each list.
