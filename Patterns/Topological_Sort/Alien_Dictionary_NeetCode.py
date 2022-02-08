'''
LeetCode #269 - Alien Dictionary

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.
If there is no solution, return "". If there are multiple solutions, return any of them.

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

----

This problem was solved using Topological Sort -> which involves Directed Acyclic Graphs (DAG)
A DAG:
- is a graph that has directed edges
- BUT NO CYCLES

So the ordering of the alien language is different from the ordering in the english alphabet
The goal is to figure out the ordering of the alien language

'''
def alienOrder(words):
  '''
  We want to create an adjacency list based on the ordering of the characters
  For every character in our entire list of words
  what we want to do is map it to a set -> set makes sure there are no duplicates
  so
  for every word in our list of words
  and then
  for every character in each word
  we want every character to be mapped to a set
  '''
  adj = { c:set() for w in words for c in w }
  
  
  # then we want to go through every pair of words
  for i in range(len(words) - 1):
    # word1 is going to be the word at index i
    # word2 is going to be the word at index i + 1
    w1, w2 = words[i], words[i + 1]
    
    # we want the minimum length of these 2 words
    minLen = min(len(w1), len(w2))
    
    # what we'll first check is the edge case we saw
    # if the minimum length of each word is the exact same
    # meaning the prefix of the words is exactly the same
    # BUT the first word is longer than the second word 
    # in which case we have an invalid ordering
    if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
      # w1[:minLen] == w2[:minLen]
      # ^ this means they have the exact same prefix meaning its an invalid ordering
      # so we return an empty string
      return ""
    
    # if this "len(w1) > len(w2) and w1[:minLen] == w2[:minLen]" is NOT the case 
    # we want to go through every single character between these words
    # our goal is to find the first different character
    # so IF the characters are the same we're NOT going to do anything
    # BUT if the characters ARE different
    for j in range(minLen):
      # if the characters are different
      # we want the first different character, so we break immediately
      # but before we break
      # we want to add this to our adjacency list
      # this says that the character in word2 comes AFTER the character in word1
      # so to indicate that we do adj[w1[j]].add(w2[j])
      # word1 is the key at index j and to that we're adding word2
      if w1[j] != w2[j]:
        adj[w1[j]].add(w2[j])
        break
    # once this is complete we can start doing out DFS
  
  # for DFS we want to keep track of visited nodes
  # for each character we're going to be mapping it to 2 values
    # False - means the character has been visited
    # True - means visited AND is in the current path
    # if its not added to the visit dictionary AT ALL that means it hasnt been visited at all
  visit = {}
  
  # we also want to maintain our result and we're going to be building this in reverse order
  # so we use a list initially so at the end we can just JOIN the characters in the list at the end
  res = []
  
  # all we need to do is pass in the current character/node that we're visiting
  def dfs(c):
    # if the character is already in visit
    # we simply return the value that is stored in visit
      # if it's already been visited -> False will be returned
      # if it's in the current path -> True will be returned
        # if DFS returns true -> that means we saw a character/node that was already in the currentPath and we saw it twiice
        # in other words if it returns True thats how you know we detected a loop
    if c in visit:
      return visit[c]
    
    # if we dont get caught above
    # we say not only has it been visited but it's also in the currentPath
    visit[c] = True
    
    # we're gonna go through every neighbor/descendant/character that comes AFTER the current character: (c)
    # so from our adjacency list that we built earlier - we're gonna go through every character
    # that's a neighbor of c -> and we're gonna run dfs on each of c's neighbors
    for nei in adj[c]:
      # if running dfs on c's neighbors returns True
      # that's how you know we have a loop -> so we can immediately return True
      if dfs(nei):
        return True
    
    # before we return we say
    # c is False -> meaning it's been visited but now its false bc its no longer in the currentPath
    visit[c] = False
    
    # THIS WAS A POST-ORDER DFS -> mainly AFTER we've done the recursive call
    # that's when we're FINALLY GOING TO SAY to our result: 
      # we can append the current character
    res.append(c)       
    # AND remember we're building this in reverse order, so once we've done the entire dfs
    # we're going to have return the result in reverse order
  
  # for every single character - and we dont NEED to start at the beginning character of the graphs
  # we can start at any single character and it'll still work out the same
  # and the reason is because we're doing it in reverse order
  # so we go through every single character in our adjacency list
  for c in adj:
    # and we call DFS on that character
    # and if the call returns true -> we return an empty string
    if dfs(c):
      # we return an empty string bc we detected a loop
      return ""
    
    # if that's not the case that's when we're actually going to return the result
    # BUT the result is a list SO we join the contents of result with an empty string -> creating the string
    # AND we HAVE to reverse the result BEFORE we perform the join
  res.reverse()
  
  return "".join(res)
