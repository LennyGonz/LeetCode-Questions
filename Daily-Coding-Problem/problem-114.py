import re

def reverse(string, delimiters):
  # Parse the string into words between delimiters using regex
  # Keep adjacent delimiters together ("greedy match")
  words = re.split('[' + delimiters + ']+', string)
  not_words = re.split('[^(' + delimiters + ')]+', string)
  if len(words) > 0 and words[-1] == '':
    words = words[:-1]
  # Reverse the list of words and convert to an iterator
  word_iter = reversed(words)

  output = []
  for d in not_words:
    output.append(d)
    try:
      output.append(next(word_iter))
    except StopIteration:
      pass

  return ''.join(output)
