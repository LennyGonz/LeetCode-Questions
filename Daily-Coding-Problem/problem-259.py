def is_winning(trie, prefix):
  root = trie.get(prefix)

  if '#' in root:
    return False
  else:
    next_moves = [prefix + letter for letter in root]
    if any(is_winning(trie, move) for move in next_moves):
      return False
    else:
      return True

def optimal_starting_letters(words):
  trie = Trie(words)
  winners = []
  
  starts = trie.trie.keys()
  for letter in starts:
    if is_winning(trie, letter):
      winners.append(letter)

  return winners

'''
Constructing the trie will take O(N * k) time, where N is the number of words in the dictionary, and k is their average length.
To find the optimal first letters, we must traverse each path in the trie, which again takes O(N * k). Therefore, this algorithm runs in O(N * k) time.
'''
