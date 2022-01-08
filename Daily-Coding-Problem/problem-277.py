def valid(data):
  first = data[0]

  if first >> 7 == 0:
    count = 0
  elif first >> 5 == 0b110:
    count = 1
  elif first >> 4 == 0b1110:
    count = 2
  elif first >> 3 == 0b11110:
    count = 3
  else:
    return False

  for byte in data[1:]:
    if byte >> 6 == 0b10:
      count -= 1
    else:
      return False

  return count == 0 

# This algorithm is O(N) in the number of bytes, since we are only performing bit shifts and equality checks on each one.
