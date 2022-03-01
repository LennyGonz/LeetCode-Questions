from collections import Counter, defaultdict
'''
LeetCode #242

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

* Questions to ask:
  - are both strings all in lowercase or mixedcase
  - 

* Immediately we can say that our base case is that the 2 strings cannot be anagrams of each other IF they are of different lengths

1) Use a HashMap to create a frequency map of all the occurances of each character in string1
    then once that is completed - iterate through string2 and reduce the value of each similar character
    FINALLY we iterate through the HashMap and if any value is NOT ZERO, we return False otherwise return True
    Time: O(s+t) - because we iterate through both strings once
    Space: O(s) - because it will hold all the characters in string1

2) We use a set - we place string1 into the set -> this allows us to potentially reduce the number of iterations IF the string contains duplicate chars
    Next we iterate through string1, using each character in the set as the pointer
    As we iterate through the chars in the set - we compare the occurances of that character in string1 and string2
      if the occurances of the current character are different in each string -> we can immediately return False otherwise True
    Time: O(s+t) - because we iterate through both strings once
    Space: O(s) - because in the worst case (all distinct chars) the set will hold all the characters in string1

3) We create a list of size 128 - since this is the total amount of characters in the ASCII table
    Therefore as we iterate through string1 we convert each character into ASCII
    We use this list as a frequency map - we iterate over string1
      for each character in string1 we increase the frequency at the index matching the ASCII representation of the current character 
    AFTER creating the frequency map of string1 - we iterate over string2
      for each character in string2 we DECREASE the frequency of the current character
    FINALLY - we iterate over the frequencyMap and if we run across any value other than 0 - we an return FALSE otherwise true
    Time: O(s+t) - because we iterate over both strings once
    Space: O(1) - Although we do use extra space, the space complexity is O(1) because the table's size stays constant no matter how large string1 is.
    * If we have to return how to fix string2 to be anagram of string1
        we iterate through the frequencyMap and whenever we come across a value that ISNT 0
        we add it to our result dictionary, where the key is the character 
        and 
        the value if negative 
          is an extra character(s) in string2
                  if positive
          is the missing character(s) in string2
    Space: O(t) - with the adjustment we use a dictionary to hold all the extra characters from string1 or hold the missing characters from string2
'''
# cheap solution
def isAnagramC(string1,string2): 
  # the inputs cannot be anagrams if they're different lengths
  if len(str(string1)) != len(str(string2)):
    return False

  return Counter(str(string1)) == Counter(str(string2))

def isAnagram1(string1, string2):
  # the inputs cannot be anagrams if they're different lengths
  if len(str(string1)) != len(str(string2)):
    return False
  
  freqMap = {}
  
  # create the character frequency map for string1
  for char in str(string1):
    if char not in freqMap:
      freqMap[char] = 0
    freqMap[char] += 1
  
  # iterate over string2 decreasing the frequency of the common characters
  for char in str(string2):
    freqMap[char] -= 1
  
  # iterate over the values of each key in string1s frequency map
  # if any values are not 0 - return False
  for value in freqMap.values():
    if value != 0:
      return False
  
  return True

def isAnagram2(string1, string2):
  # the inputs cannot be anagrams if they're different lengths
  if len(str(string1)) != len(str(string2)):
    return False
  
  for char in set(str(string1)):
    if str(string1).count(char) != str(string2).count(char):
      return False
  
  return True
  
def isAnagram3(s,t):  
  # The entire ASCII table contains 128 characters
  # since we cover all possible characters this list cannot grow - it will always be of size 128 - therefore constant space
  inputFreqMap = [0]*128
  
  # if asked how can we make t an anagram of s - we return this hashMap
  res = defaultdict()
  
  for i in str(s):
    # The ord() function returns an integer representing the Unicode character.
    inputFreqMap[ord(i)]+=1

  for i in str(t):
    inputFreqMap[ord(i)]-=1
  
  # answers the standard anagram question
  for i in inputFreqMap:
    if i!=0:
      return False
  return True
'''
  # if asked to identify the characters needed to make string1 & string 2 anagrams
  for index, value in enumerate(inputFreqMap):
    if value != 0:
      res[chr(index)] = value

  return res
'''

def main():
  string1 = "anagram"
  string2 = "nagaram"
  
  print(isAnagramC(string1, string2)) # True
  print(isAnagram1(string1, string2)) # True
  print(isAnagram2(string1, string2)) # True
  print(isAnagram3(string1, string2)) # True
  
  num1 = 123
  num2 = 321
  
  print(isAnagramC(num1, num2)) # True
  print(isAnagram1(num1, num2)) # True
  print(isAnagram2(num1, num2)) # True
  print(isAnagram3(num1, num2)) # True

main()
