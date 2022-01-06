from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
  if endWord not in wordList:
    return 0
  
  # create the adjacency list
  nei = defaultdict(list)
  
  # add beginWord to wordList
  wordList.append(beginWord)
  
  for word in wordList:
    for j in range(len(word)):
      pattern = word[:j] + "*" + word[j+1:]
      nei[pattern].append(word)
  
  visited = set([beginWord])
  queue = deque([beginWord])
  res = 1
  
  while queue:
    for _ in range(len(queue)):
      word = queue.popleft()
      
      if word == endWord:
        return res

      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j+1:]
        
        for neiWord in nei[pattern]:
          if neiWord not in visited:
            visited.add(neiWord)
            queue.append(neiWord)
      
    res += 1
  
  return 0
  
bW = "hit"
eW = "cog"
wL = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(bW,eW,wL)) # 5
