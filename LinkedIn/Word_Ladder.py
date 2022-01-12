from collections import defaultdict
from collections import deque

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
      return 0
    
    nei = defaultdict(list)
    
    wordList.append(beginWord)
    
    for word in wordList:
      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j+1:]
          
        nei[pattern].append(word)
    
    visited = set([beginWord])
    q = deque([beginWord])
    res = 1
    
    while q:
      for i in range(len(q)):
        word = q.popleft()
          
        if word == endWord:
            return res
          
        for j in range(len(word)):
          pattern = word[:j] + "*" + word[j+1:]
              
          for neiWord in nei[pattern]:
            if neiWord not in visited:
              visited.add(neiWord)
              q.append(neiWord)
      res += 1
    
  return 0
