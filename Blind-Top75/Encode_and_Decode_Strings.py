'''
LeetCode #271

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
------------------------------------------------------------------------------------------------------------------------------------------------------

This problem seems straight forward, however if you encode the list of strings
  the issue becomes when you decode it...
    how do you determine where one word ends and another begins

What comes to mind to fix this is
  we encode each string with its length and some sort if a delimiter
  the length will tell us where one word begins and ends
  the delimiter is useful in case the word also contains a number, so we use it to separate the length and the word itself avoiding such confusion

Therefore when we decode the encoded string, we can iterate through it, collection the character till we reach the delimiter
convert those characters into an integer, then use that integer to determine the length of the word we encoded

Time: O(N) - where N is the total # of words
Space: O(1) - runs in constant space
'''

class Codec:
  def encode(self, strs):
    # we'll encode our list of strings into 1 long string
    res = ""
    
    # as we iterate through the list
    # we first append the length of the word
    # we then append the delimiter
    # then finally add the string
    for s in strs:
      res += str(len(s)) + "#" + s
    
    print(res)
    return res
    # at the end of the for-loop, all strings have been encoded with this pattern
    # lengthOfString#string -> ex string=Lenny -> 5#Lenny
  
  def decode(self, s):
    # we have to decode the long string BACK into a list of strings => res will hold them
    res = []
    
    # we need a pointer to keep track of where we are in the encoded string
    index = 0
    
    # while index is inbounds of the encoded string
    while index < len(s):
      # we use this variable to iterate through the string and help find the length
      j = index
      
      # if we haven't reach the delimiter we're still finding the length of the word
      while s[j] != '#':
        j += 1
      
      # once we find the length we need to cast it to an integer
      length = int(s[index:j])
      
      # j+1 skips the delimiter(#) and points to the first character in the string
      # j+1+length point to the word we want to add to our list
      res.append(s[j+1 : j+1+length])
      
      # we need to update our index pointer, so it points to the next encoded word
      index = j+1+length
    
    return res

# driver code
codec = Codec()

strs = ["Lenny", "Benny", "Jenny", "Kenny"]

print(codec.decode(codec.encode(strs)))
