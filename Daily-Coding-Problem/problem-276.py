def build_table(pattern):
  matches = [0 for _ in range(len(pattern))]

  length = 0
  for i in range(1, len(pattern)):
    if pattern[i] == pattern[length]:
      length += 1
      matches[i] = length

    else:
      while length != 0:
        length = matches[length - 1]
      matches[i] = 0

  return matches

def find_match(string, pattern):
  matches = build_table(pattern)

  i, j = 0, 0
  while i < len(string):
    if string[i] == pattern[j]:
      i += 1; j += 1

      if j == len(pattern):
        return i - j

    else:
      if j > 0:
        j = matches[j - 1]
      else:
        i += 1

  return None
