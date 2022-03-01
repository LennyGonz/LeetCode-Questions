'''
LeetCode #139

Brute-Force: we traverse the string, char by char, constantly checking the dictionary to see if the word we have is in the string
i.e) string = leetcode & wordDict = [leet,code]
"l" is "l" in wordDict ? NO
"le" is "le" in wordDict ? NO
"lee" is "lee" in wordDict ? NO
"leet" is "leet" in wordDict ? YES

The problem with this approach is, if we break at this point "leet" will the remainder of the chars in the string build to be words in wordDict?

SO we'll work based off word length

1. we start at the first position - bc we know if we can find a word in wordDict that matches, then the subproblem is going to be finding a word in wordDict that can match the remainder of the string

- so we're not checking every prefix
- we're going to have decisions in our decision tree based on the number of words in the wordsDict 

so if inputString = "leetcode" and wordDict = ["neet","leet","code"]
          i=0
    neet  leet  code (3 decisions)

so when we try leet on s -> neet is 4 characters long, we check the first 4 characters of s (inputString) 
  - they don't match bc 1 character is off

code on s -> code is 4 characters long, we check the first 4 characters of s
  - they dont match at all

leet on s -> leet is 4 characters long, and matches perfectly

now we have "code" left in the inputString
we repeat the same process as above

so when we try neet on s -> neet is 4 characters long, we check the first 4 characters of s (inputString) 
  - they don't match
  
so when we try neet on s -> leet is 4 characters long, we check the first 4 characters of s (inputString) 
  - they don't match

code on s -> code is 4 characters long, we check the first 4 characters of s
  - they match!
  
So notice the relation:

so if inputString = "leetcode" and wordDict = ["neet","leet","code"]
          i=0
    neet  leet  code (3 decisions)
            |         
      first 4 chars matches leet
          i = 4
    neet  leet  code
                  |
                next 4 chars matches code
                      i = 8

The length of the inputString = 8, so from 0 -> 4 -> 8, 8 is right after the input string
Therefore, we know we're able to match the entire string

So in order to do this we need to be able to track the progress of words fitting into our string, so we create boolean array

if i = 0
leet == leet

i moves to index 4
code == code

i moves to index 8
index 8 is out of bounds, but it means 2 words matched perfectly with our string, so we can set index 8 to True in a cache

So if we work backwords starting with index 8 = True

we'll find code

if (i + len(w)) <= len(inputString) and s[i:i+len(w)] == w

i = 4 and len(code) = 4 and s[4:4+4] == "code" * spliciing end is exlusive so [4:7]
"leetcode" and wordDict = ["neet","leet","code"]
 01234567
4 + 4 <= 8 True and code == code

then we can say dp[i] = dp[i+len(w)]
dp[4] = dp[4 + 4] = dp[8] (which is our base case)
'''

def wordBreak(s, wordDict):
  # we initialize our cache
  # we make it the size of the input string + 1
  # + 1 - because thats the out of bounds position we're using as our base case
  dp = [False] * (len(s)+1)

  # base case - if we match words from wordsDict to words in our input string, we'll reach the Len(S) + 1 position
  dp[len(s)] = True
  
  # we traverse our input string in reverse
  # we're going to go through every position "i" in the length of the string
  # starting at the last index -> working our way to the beginning
  for i in range(len(s)-1, -1,-1):
    
    # for each position i, we want to try every length word in our wordDict
    # and see if the word matches this portion of the input string
    for w in wordDict:
      
      # if we have to see IF the starting at position i the string s even has enough # of characters
      # for the word in wordDict to be compared to it
      # if (i + len(w)) <= len(w)) that means s has enough characters for w to compare
      # and
      # if substring of s starting at position i till len(word) is the same as the word in wordDict
      if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
        
        # this relation is what will make this work
        dp[i] = dp[i+len(w)]
      
      # if we find a single way to word break the string
      # we can stop the loop, we don't have to look at every word in the wordDict
      # we just need at least 1 way to word break the input string
      if dp[i]:
        break
  
  # we iterate till we reach the front of the input string and if s can be segmented into a space-separated sequence
  # of one or more words in wordDict than dp[0] = True
  return dp[0]

string = "leetcode"
print(len(string))
wordDictionary = ["leet","code"]
print(wordBreak(string, wordDictionary))

'''
Time complexity : O(n^3) There are two nested loops, and substring computation at each iteration. Overall that results in O(n^3) time complexity.

Space complexity : O(n). Length of dp array is n+1.
'''
