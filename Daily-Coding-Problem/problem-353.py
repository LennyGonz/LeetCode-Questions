def largest_rectangle(array):
  stack = []
  max_area = 0

  # Append a zero to handle cases of non-decreasing sequences.
  array.append(0)

  for right_index, rect in enumerate(array):
    while stack and rect < array[stack[-1]]:
      height = array[stack.pop()]

      left_index = stack[-1] if stack else -1
      width = right_index - (left_index + 1)

      max_area = max(max_area, height * width)

    stack.append(right_index)

  return max_area
