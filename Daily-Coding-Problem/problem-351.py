import re

STOPWORDS = set(['a', 'in', 'or', 'the', 'to'])

def normalize(sentence):
  sentence = re.sub('[^A-Za-z ]', '', sentence)

  words = sentence.lower().split()

  return [word for word in words if word not in STOPWORDS]

def disambiguate(sentence, words, meanings):
  true_senses = {}

  sentence = set(normalize(sentence))

  for word in words:
    max_overlaps = 0; true_senses[word] = None

    for sense in meanings[word]:
      definition = set(normalize(sense))
      overlaps = definition.intersection(sentence)

      if len(overlaps) > max_overlaps:
        max_overlaps = len(overlaps)
        true_senses[word] = sense

  return true_senses
