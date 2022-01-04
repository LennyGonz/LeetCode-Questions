import string

UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
SPACE = [' ']
SEP = [',', ';', ':']
TERM = ['.', '?', '!', '‽']

def check_sentences(stream):
  state = 0
  sentence = []

  while stream:
    char = stream.__next__()
    sentence.append(char)

    if char in UPPER and state == 0:
      state = 1

    elif char in LOWER and state in (1, 2, 3):
      state = 2

    elif char in SPACE and state in (1, 2, 4):
      state = 3

    elif char in SEP and state == 2:
      state = 4

    elif char in TERM and state == 2:
      yield ''.join(sentence)
      state = 0
      sentence = []

    else:
      sentence = []
