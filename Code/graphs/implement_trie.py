class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    
    for char in word:
      if char not in curr.children:
        curr.children[char] = TrieNode()
      curr = curr.children[char]
    
    curr.endOfWord = True
    
  def search(self, word):
    curr = self.root
    
    for char in word:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    
    return curr.endOfWord
  
  def startsWith(self, prefix):
    curr = self.root
    
    for char in prefix:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    
    return True
