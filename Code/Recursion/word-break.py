def wordBreak(s, wordDict):
  dp = [False] * (len(s)+1)
  print("1-dp",dp)
  dp[len(s)] = True
  print("2-dp",dp)
  
  for i in range(len(s)-1, -1,-1):
    for w in wordDict:
      if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
        dp[i] = dp[i+len(w)]
      if dp[i]:
        print("i= ", i)
        break
  return dp[0]

string = "leetcode"
print(len(string))
wordDictionary = ["leet","code"]
print(wordBreak(string, wordDictionary))
