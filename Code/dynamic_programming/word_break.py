# LeetCode Problem 139

def wordBreak(string, wordDic):
  dp = [False] * (len(string) + 1)
  dp[len(string)] = [True]
  
  for index in range(len(string)-1,-1,-1):
    for word in wordDic:
      if (index + len(word)) <= len(string) and string[index:index+len(word)] == word:
        dp[index] = dp[index+len(word)]
        
        if dp[index]:
          break
  
  return dp[0]

def main():
  string1 = "leetcode"
  wordDic1 = ["leet","code"]
  
  string2 = "applepenapple"
  wordDic2 = ["apple","pen"]
  
  print("string: 'leetcode' and the wordDic: ['leet','code'] answer ->", wordBreak(string1, wordDic1))
  print("string: 'applepenapple' and the wordDic: ['apple','pen'] answer ->", wordBreak(string2, wordDic2))

main()

'''
run time: LeetCode says O(n^3) -> There are two nested loops, and substring computation at each iteration. Overall that results in O(n^3) time complexity
Space: O(n) -> Length of dp array is n+1.
'''
