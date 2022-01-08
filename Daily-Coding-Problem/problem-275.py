import itertools

def look_and_say(num):
  result = '1'

  for _ in range(num - 1):
    tmp = ''
    for char, group in itertools.groupby(result):
      count = len(list(group))
      tmp += (str(count) + char)
    result = tmp

  return result
