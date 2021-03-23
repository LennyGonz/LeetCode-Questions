def add_to_trie(s, trie):
  if not s:
    return trie
  
  character = s[0]
  if character not in trie:
    trie[character] = dict()
  
  trie[character] = add_to_trie(s[1:], trie[character])

  return trie

def get_dictionary_trie(dictionary):
  trie = dict()
  for word in dictionary:
    trie = add_to_trie(word, trie)
  print("trie", trie)
  return trie

def get_possible_completions(trie):
  possible_completions = list()
  for character in trie:
    if trie[character]:
      child_completions = get_possible_completions(trie[character])
      for child_completion in child_completions:
        possible_completions.append(character + child_completion)
    
    else:
      possible_completions.append(character)
  return possible_completions

def get_autocomplete_suggestions(s, dictionary):
  trie = get_dictionary_trie(dictionary)

  current_trie = trie
  for character in s:
    if character not in current_trie:
      return []
    current_trie = current_trie[character]
  
  completions = get_possible_completions(current_trie)
  completions = [s + x for x in completions]

  return completions

print(get_autocomplete_suggestions('de', ['dog', 'deer', 'deal']))

'''
The naive solution here is very straightforward: we need to only interate over the dictionary and check if each word starts with our prefix
If it does, then add it to our set of results and then return it once we're done
'''

WORDS = ['foo', 'bar', ...]
def autocomplete(s):
  results = set()

  for word in WORDS:
    if word.startswith(s):
      results.add(word)
  return results

'''
This runs in O(n) time, where n is the number of words in the dictionary.
Let's think about making this more efficient. We can preprocess the words, but what data structure would be best for our problem?

If we pre-sort the list, we could use binary search to find the first word that includes our prefix and then the last, and return everything in between

Alternatively, we could use a tree fr this. Not a binary tree, but a tree where each child represents one character of the alphabet
For example, let's say we had the words 'a' and 'dog' in our dictionary. Then the tree would look like this:

  x
 / \
a   d
     \
      o
       \
        g

Then, to find all words beginning with 'do', we could start at the root, go into the 'd' child, and then the 'o', child, and gather up all the words under there

We would also some sort of terminal value to mark whether or not 'do' is actually a word in our dictionary or not

This data structure is known as a trie

So the idea is to preprocess the dictionary into this tree, and then when we search for a prefix, go into the trie and get all the words under that prefix node
and return those

While the worst-case runtime would still be O(n) if all the search results have that prefix, if the words are uniformly distributed across the alphabet, it should be much faster on average since we no longer have to evaluate words that don't start with our prefix
'''

ENDS_HERE = '__ENDS_HERE'

class Trie(object):
  def __init__(self):
    self._trie = {}

  def insert(self, text):
    trie = self._trie
    for char in text:
      if char not in trie:
        trie[char] = {}
      trie = trie[char]
    trie[ENDS_HERE] = True
  
  def elements(self, prefi):
    d = self._trie
    
    for char in prefix:
      if char in d:
        d = d[char]
      else:
        return []
    return self._elements(d)
  
  def _elements(self, d):
    result = []

    for c, v in d.items():
      if c == ENDS_HERE:
        subresult = ['']
      else:
        subresult = [c + s for s in self._elements(v)]
      result.extend(subresult)
    return result

trie = Trie()

for word in words:
  trie.insert(word)

def autocomplete2(s):
  suffixes = trie.elements(s)
  return [s + w for w in suffixes]
