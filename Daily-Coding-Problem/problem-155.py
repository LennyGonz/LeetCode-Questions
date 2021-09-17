def majority(elements):
  for i, e in enumerate(elements):
    if i == 0 or count == 0:
      majority = e
      count = 1
    elif majority == e:
      count += 1
    else:
      count -= 1
  return majority
