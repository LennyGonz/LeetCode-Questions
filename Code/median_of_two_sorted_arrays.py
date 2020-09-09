'''
Time Complexity: O(log(n+m))
Space Complexity: O(log(n+m))
'''

def median(A, B):
  m, n = len(A), len(B)
  print("m:",m,"|","n:",n)
  if m > n:
    A, B, m, n = B, A, n, m
    print("A:",A,"||","B",B,"||","m:",m,"||","n:",n)
  if n == 0:
    raise ValueError
  
  imin, imax, half_len = 0, m, (m + n + 1) // 2
  print("imin:",imin,"||","imax",imax,"||","half_len",half_len)
  while imin <= imax:
    i = (imin + imax) // 2
    j = half_len - i
    print("i:",i,"||","j",j)
    if i < m and B[j - 1] > A[i]:
      # i is too small, must increase it
      imin = i + 1
      print("imin inside the if statement:",imin)
    elif i > 0 and A[i-1] > B[j]:
      # i is too big, must decrease it
      imax = i - 1
      print("imax inside of the elif statement",imax)
    else:
      # i is perfect
      if i == 0:
        max_of_left = B[j - 1]
        print("else -> if -> max_of_left", max_of_left)
      elif j == 0:
        max_of_left = A[i - 1]
        print("else -> elif -> max_of_left", max_of_left)
      else:
        max_of_left = max(A[i - 1], B[j - 1])
        print("else -> else -> max_of_left:", max_of_left)

      if (m + n) % 2 == 1:
        print("1st return statement - returning max_of_left", max_of_left)
        return max_of_left

      if i == m:
        min_of_right = B[j]
        print("if -> min_of_right:",min_of_right)
      elif j == n:
        min_of_right = A[i]
        print("elif -> min_of_right",min_of_right)
      else:
        min_of_right = min(A[i], B[j])
        print("else -> min_of_right",min_of_right)

      print("max_of_light",max_of_left, "||", "min_of_right",min_of_right, "||", "return=",((max_of_left+min_of_right)/2))
      return (max_of_left + min_of_right) // 2.0

input1 = [1,3]
input2 = [2]
print(median(input1, input2))
