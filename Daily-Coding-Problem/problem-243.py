def can_partition(array, limit, k):
  total = 0
  partitions = 1

  for num in array:
    if total + num > limit:
      total = num
      partitions += 1
      if partitions > k:
        return False
    else:
      total += num

  return True
