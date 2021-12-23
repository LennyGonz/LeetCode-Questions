from collections import OrderedDict

def order_letters(words):
  n = len(words[2])

  letters = OrderedDict()
  for i in range(n - 1, -1, -1):
    for word in words:
      if word[i] not in letters:
        letters[word[i]] = None

  return letters

def normalize(word, n):
  diff = n - len(word)
  return ['#'] * diff + word

def cryptanalyze(problem):
  words = list(map(list, problem))

  n = len(words[2])
  words[0] = normalize(words[0], n)
  words[1] = normalize(words[1], n)

  letters = order_letters(words)
  unassigned = [letter for letter in letters if letter != '#']
  nums = set(range(0, 10))

  return solve(letters, unassigned, nums, words)

'''
To analyze the time complexity, we can look at each function.
For is_valid, we check up to three words for each column, so this will be O(N), where N is the number of letters in the sum.
If we let C be the number of distinct characters, then we will call solve O(C!) times, since each call will reduce the number of characters to solve by one.
Since each solve attempt requires a validity check, the overall complexity will be O(N * C!).
'''
