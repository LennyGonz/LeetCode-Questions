def find_continuous_k(list, k):
  previous = dict()
  sum = 0
  # sublist starting at the zeroth position work.
  previous[0] = -1
  for last_idx, item in enumerate(list):
    sum += item
    previous[sum] = last_idx
    first_idx = previous.get(sum - k)
    if first_idx is not None:
      return list[first_idx + 1:last_idx + 1]
  return None
