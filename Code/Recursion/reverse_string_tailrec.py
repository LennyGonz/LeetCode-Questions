def reverseStr(s):
  def helper(start, end, ls):
  #base case
    if start >= end:
      return

    ls[start], ls[end] = ls[end], ls[start]

    return helper(start+1, end-1, ls)
  helper(0, len(s)-1, s)

# this works on leetcode
# python does not let you change their characters in place

print(reverseStr("hello"))
