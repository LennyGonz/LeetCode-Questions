from collections import Counter

def starting_concatenations(s, words):
  if not words:
    return []

  k = len(words[0])
  result = []

  for i in range(k):
    c = Counter(words)
    for j in range(i + k, len(s) + 1, k):
      word = s[j - k: j]
      c[word] -= 1

      # No possible match: restore words and move i up.
      while c[word] < 0:
        c[s[i:i + k]] += 1
        i += k

      # Matched all words
      if i + k * len(words) == j:
        result.append(i)
  return result
