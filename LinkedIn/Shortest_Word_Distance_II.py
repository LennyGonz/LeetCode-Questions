'''
LeetCode #244

Here they ask you design a data structure, and 1 method that comes with the data structure 
- the method -> returns the shortest distance between 2 words, we literally just solved that (shortest word distance I)

So all thats left is creating the data structure

We simply initilize a hashMap and iterate over the input array
the key is the word and the value will be a list of indicies where the word occured in the inputlist

We populate the hashmap in the constructor method
'''

class WordDistance:
  def __init__(self, wordsDict):
    self.wordMap = {}
    
    for index, word in enumerate(wordsDict):
      if word not in self.wordMap:
        self.wordMap[word] = []
      self.wordMap[word].append(index)

  def shortestDistance(self, word1, word2):
    list1 = self.wordMap[word1]
    list2 = self.wordMap[word2]
    
    p1, p2 = 0, 0
    res = float("inf")
    
    while (p1 < len(list1) and p2 < len(list2)):
      res = min(res, abs(list1[p1] - list2[p2]))
      
      # we increase the index of the smaller value, since increasing greater value won't give you the shorter distance
      if list1[p1] < list2[p2]:
        p1 += 1
      
      else:
        p2 += 1
    
    return res

