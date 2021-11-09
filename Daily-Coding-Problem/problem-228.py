def get_largest_value(nums):
  nums = [str(x) for x in nums]
  length = len(max(nums, key=len))

  normalized = []
  for i, x in enumerate(nums):
    element = x * (length // len(x) + 1)
    normalized.append(element[:length])

  ordered = sorted(zip(nums, normalized), key=lambda x: x[1], reverse=True)

  return ''.join([x[0] for x in ordered])
