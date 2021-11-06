def standardize(path):
  stack = []
  path = path.split("/")

  for segment in path:
    if segment == ".":
      continue
    elif segment == "..":
      if len(stack) > 1:
        stack.pop()
    else:
      stack.append(segment)

  return "/".join(stack)
