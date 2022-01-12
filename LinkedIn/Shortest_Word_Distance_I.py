'''
The distance between any two positions: i1 and i2 in an array is |i1 - i2|

So to find the shortest distance between word1 and word2, we need to traverse the input array and find all occurrences of word1 and word2 and store the indices of where you can find those 2 words in respective lists

Once we're done populating the lists of occurrences for word1 and word2
We iterate over both lists calculating the minimum distances
'''

def shortestDistance(wordsDict, word1, word2):
  list1 = []
  list2 = []
  
  p1, p2 = 0, 0
  res = float("inf")
  
  for index, word in enumerate(wordsDict):
    if word == word1:
      list1.append(index)
    elif word == word2:
      list2.append(index)
  
  while (p1 < len(list1) and p2 < len(list2)):
    res = min(res, abs(list1[p1] - list2[p2]))
    
    if list1[p1] < list2[p2]:
      p1 += 1
    
    else:
      p2 += 1
  
  return res

'''
Time: O(N+M) 
Space: O(N+M) - list for word1 and word2
'''

'''
OPTIMAL APPROACH

1. IF we keep two indices i1 and i2 where we store the most recent locations of word1 and word2

2. Each time we find a new occurrence of one of the words,

3. we do not need to search the entire array for the other word

4. since we already have the index of its most recent occurrence.
'''

def shortestDistance(wordsDict, word1, word2):
  minDistance = len(wordsDict)
  position1 = -1
  position2 = -1
  
  for i in range(len(wordsDict)):
    if wordsDict[i] == word1:
      position1 = i
    
    elif wordsDict[i] == word2:
      position2 = i
    
    if position1 != -1 and position2 != -1:
      minDistance = min(minDistance, abs(position1-position2))
  
  return minDistance

'''
Time: O(N) - N is the total number of elements in wordsDict - we did this in one-pass
Space: O(1) - algorithm runs in constant space
'''
