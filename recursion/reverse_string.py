def reverse_(str):
  res = ""
  for char in str[::-1]:
    res += char
  
  return res

print(reverse_("hello"))

def reverse(Str):
  if Str == "":
    return ""
  else:
    return reverse(Str[1:]) + Str[0]

print(reverse("hello"))

def reverseString(s):
  """
  :type s: List[str]
  :rtype: void Do not return anything, modify s in-place instead.
  """
  def helper(start, end, ls):
    if start >= end:
      return

    # swap the first and last element
    ls[start], ls[end] = ls[end], ls[start]        

    return helper(start+1, end-1, ls)

  helper(0, len(s)-1, s)

reverseString("hello")
