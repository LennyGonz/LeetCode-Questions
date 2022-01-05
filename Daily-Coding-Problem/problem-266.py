from collections import defaultdict

def create_wordmap(dictionary):
  wordmap = defaultdict(list)
  for word in dictionary:
    wordmap[tuple(sorted(word))].append(word)
  return wordmap

from string import ascii_uppercase

def step_words(word, dictionary):
  wordmap = create_wordmap(dictionary)

  step_words = []
  for letter in ascii_uppercase:
    key = tuple(sorted(word + letter))
    if wordmap[key]:
      step_words.extend(wordmap[key])

  return step_words
