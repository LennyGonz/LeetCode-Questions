def round_numbers(array):
  result = [floor(x) for x in array]

  leftover = int(round(sum(array)) - sum(result))

  diffs = sorted(enumerate(array), key=lambda x: x[1] - floor(x[1]))

  while leftover > 0:
    result[diffs.pop()[0]] += 1
    leftover -= 1

  return result
