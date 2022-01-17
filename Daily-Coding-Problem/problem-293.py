def find_cost(x, h, stones):
  heights = []
  for i in range(len(stones)):
    heights.append(h - abs(x - i))

  costs = [s - h for (s, h) in zip(stones, heights)]
  if any(c < 0 for c in costs):
    return False

  return sum(costs)

def build_pyramid(stones):
  left = [0 for _ in range(len(stones))]
  right = [0 for _ in range(len(stones))]

  left[0] = 1
  for i in range(1, len(stones)):
    left[i] = min(stones[i], left[i - 1] + 1)

  right[-1] = 1
  for i in range(len(stones) - 2, -1, -1):
    right[i] = min(stones[i], right[i + 1] + 1)

  min_heights = [min(l, r) for (l, r) in zip(left, right)]

  center = min_heights.index(max(min_heights))
  height = min_heights[center]
  cost = find_cost(center, height, stones)

  return cost
