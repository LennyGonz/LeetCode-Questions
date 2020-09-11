# l1 = [5, 6, 4]
# l2 = [1]

# while l1:
#   print("hello world")
#   break

# while l2:
#   print("never reaches")
#   break

def median(input1, input2):
  length_of_input1, length_of_input2 = len(input1), len(input2)
  print("length_of_input1:",length_of_input1,"|","length_of_input2:",length_of_input2)
  if length_of_input1 > length_of_input2:
    input1 = input2
    input2 = input1
    length_of_input1 = length_of_input2
    length_of_input2 = length_of_input1 
    print("input1:",input1,"||","input2",input2,"||","length_of_input1:",length_of_input1,"||","length_of_input2:",length_of_input2)
  if length_of_input2 == 0:
    raise ValueError
  
  imin = 0
  imax = length_of_input1
  half_len = (length_of_input1 + length_of_input2 + 1) // 2
  print("imin:",imin,"||","imax",imax,"||","half_len",half_len)
  while imin <= imax:
    input1_partition = (imin + imax) // 2
    input2_partition = half_len - input1_partition
    print("input1_partition:",input1_partition,"||","input2_partition",input2_partition)
    if input1_partition < length_of_input1 and input2[input2_partition - 1] > input1[input1_partition]:
      # input1_partition is too small, must increase it
      imin = input1_partition + 1
      print("imin inside the if statement:",imin)
    elif input1_partition > 0 and input1[input1_partition-1] > input2[input2_partition]:
      # input1_partition is too big, must decrease it
      imax = input1_partition - 1
      print("imax inside of the elif statement",imax)
    else:
      # input1_partition is perfect
      if input1_partition == 0:
        max_of_left = input2[input2_partition - 1]
        print("else -> if -> max_of_left", max_of_left)
      elif input2_partition == 0:
        max_of_left = input1[input1_partition - 1]
        print("else -> elif -> max_of_left", max_of_left)
      else:
        max_of_left = max(input1[input1_partition - 1], input2[input2_partition - 1])
        print("else -> else -> max_of_left:", max_of_left)

      if (length_of_input1 + length_of_input2) % 2 == 1:
        print("1st return statement - returning max_of_left", max_of_left)
        return max_of_left

      if input1_partition == length_of_input1:
        min_of_right = input2[input2_partition]
        print("if -> min_of_right:",min_of_right)
      elif input2_partition == length_of_input2:
        min_of_right = input1[input1_partition]
        print("elif -> min_of_right",min_of_right)
      else:
        min_of_right = min(input1[input1_partition], input2[input2_partition])
        print("else -> min_of_right",min_of_right)

      print("max_of_light",max_of_left, "||", "min_of_right",min_of_right, "||", "return=",((max_of_left+min_of_right)/2))
      return (max_of_left + min_of_right) / 2.0

input1 = [1,3,5,6]
input2 = [2,4]
print(median(input1, input2))
