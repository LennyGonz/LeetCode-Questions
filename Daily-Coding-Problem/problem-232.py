from collections import defaultdict

class Trie:
  def __init__(self):
    self.letters = defaultdict(dict)
    self.total = 0

class PrefixMapSum:
  def __init__(self):
    self.root = Trie()
    self.map = {}

  def insert(self, key: str, value: int):
    # If the key already exists, increment prefix totals by the difference of old and new values.
    value -= self.map.get(key, 0)
    self.map[key] = value

    curr = self.root
    for char in key:
      curr = curr.letters.setdefault(char, Trie())
      curr.total += value

  def sum(self, prefix):
    curr = self.root
    for char in prefix:
      curr = curr.letters[char]
    return curr.total if curr else 0
