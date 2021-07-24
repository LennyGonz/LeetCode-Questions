def can_reach_end(hops):
  steps_left = 1

  for i in range(len(hops) - 1):
    steps_left = max(steps_left - 1, hops[i])
    if steps_left == 0:
      return False
  return True
