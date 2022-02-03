'''
We are given two words - we want to create a sequence that'll take us from begin word to end word
Where endWord definitely needs to be apart of wordList -> beginWord doesnt

1 restriction we have to follow is that:

every adjacent pair of words in the sequence can only differ by a single character

so lucky us, every single word including the beginWord and endWord and every word in wordList
is guaranteed to be the exact same length

so it'll be easy to take 2 words and fiure out what's the difference between them

So what we do is we create an adjacency list for every pattern we can create given the words we're given

i.e) hot -> *ot, h*t, ho*
    dot -> *ot, d*t, do*

The key in the adjacency list is the pattern and the value will be a list of words that fall into this pattern

{"*ot": ["hot","dot","lot"]}

So if we wanted all the neighbors of "hot" in our adjancency list we just do:

adjacency_list["*ot"] = [hot,dot,lot]

The computation for this will be O(n*m^2) -> iterating over the entire word O(M) -> add each word to the list O(M) and going through the wordList O(N)

We approach this with BFS

We're never going to visit the same neighbor twice, but we will potentially visit each edge once *but no revisit

# of edges = # of words (N^2)

To find each neighbor, we do M operation, where M is the length of a particular word
'''
from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
  # base case - if endWord not in wordList return 0 - because that's a requirement
  if endWord not in wordList:
    return 0
  
  # create the adjancency list
  nei = defaultdict(list)
  
  # append beginWord to our wordList
  wordList.append(beginWord)
  
  # iterate over every word in wordList
  # create all the possible patterns for that word
  # each pattern of that word becomes a key, and we append the current word to each pattern's list
  for word in wordList:
    for j in range(len(word)):
      # create the pattern
      pattern = word[:j] + "*" + word[j+1:]
      
      # append the word to the new pattern's list
      nei[pattern].append(word)
    
    # our visit set, our sequence has to begin wih beginWord
    # and we dont want to revisit the same position twice
    visited = set([beginWord])
    
    # we use a queue for BFS, and again we start at beginWord
    q = deque([beginWord])
    
    # the length of this sequence has to be at least one... beginWord
    res = 1
    
    # we want to go though the entire layer, then increment our result by 1, Only when we're done with a layer
    # then continue going layer by layer till the queue is empty
    while q:
      for _ in range(len(q)):
        word = q.popleft()
        
        # if we find endWord then we're done
        if word == endWord:
          # return the length of the sequence
          return res
        
        # if we havent found endword, we take the neighbors of the current word we're on
        # and add them to the queue
        # but before we can even add them to the queue
        # we need to figure out all the patterns that this word falls into AND THEN
        # we need to get all the other words that fall into the exact same pattern
        for j in range(len(word)):
          pattern = word[:j] + "*" + word[j+1:]
              
          for neiWord in nei[pattern]:
            if neiWord not in visited:
              visited.add(neiWord)
              q.append(neiWord)
      res += 1
    
  return 0
bW = "hit"
eW = "cog"
wL = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(bW,eW,wL)) # 5
