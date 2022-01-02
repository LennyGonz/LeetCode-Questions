# LeetCode Question 394

def decodeString(s):
  stack = []
  
  for i in range(len(s)):
    # we want to iterate through the entire input string and add it to the stack UNLESS it's a closing bracket
    if s[i] != "]":
      stack.append(s[i])

    # If we have reach a closing bracket we can start to decode
    else:
      substr = ""
      
      # while the element at the top of the stack IS NOT an opening bracket, continue popping elements and contrusting the substring
      while stack[-1] != "[":
        substr = stack.pop() + substr
      
      # We need to remove the opening bracket from our stack because
      # 1) we only needed it as a marker to stop from constructing the substring within the brackets
      # 2) we want the integer that tells us how many times to multiply the substring by
      stack.pop()
      
      # We need to start constructing the integer
      k = ""
      
      while stack and stack[-1].isdigit():
        k = stack.pop() + k
      
      # We NOW have our integer AND the substring within a bracket pair so, lets add it and continue decoding the inner substrings
      stack.append(int(k) * substr)
  
  return "".join(stack)

print(decodeString("3[a]2[bc]")) # "aaabcbc"
print()
print(decodeString("3[a2[c]]")) # "accaccacc"
print()
print(decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
print()
print(decodeString("abc3[cd]xyz")) # "abccdcdcdxyz"
