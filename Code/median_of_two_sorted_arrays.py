'''
Time Complexity: O(log(n+m))
Space Complexity: O(log(n+m))
'''

def median(input1, input2):
  length_of_input1, length_of_input2 = len(input1), len(input2)

  if length_of_input1 > length_of_input2:
    input1 = input2
    input2 = input1
    length_of_input1 = length_of_input2
    length_of_input2 = length_of_input1 

  if length_of_input2 == 0:
    raise ValueError
  
  imin = 0
  imax = length_of_input1
  half_len = (length_of_input1 + length_of_input2 + 1) // 2

  while imin <= imax:
    input1_partition = (imin + imax) // 2
    input2_partition = half_len - input1_partition

    if input1_partition < length_of_input1 and input2[input2_partition - 1] > input1[input1_partition]:
      # input1_partition is too small, must increase it
      imin = input1_partition + 1

    elif input1_partition > 0 and input1[input1_partition-1] > input2[input2_partition]:
      # input1_partition is too big, must decrease it
      imax = input1_partition - 1

    else:
      # input1_partition is perfect
      if input1_partition == 0:
        max_of_left = input2[input2_partition - 1]

      elif input2_partition == 0:
        max_of_left = input1[input1_partition - 1]

      else:
        max_of_left = max(input1[input1_partition - 1], input2[input2_partition - 1])

      if (length_of_input1 + length_of_input2) % 2 == 1:
        return max_of_left

      if input1_partition == length_of_input1:
        min_of_right = input2[input2_partition]

      elif input2_partition == length_of_input2:
        min_of_right = input1[input1_partition]

      else:
        min_of_right = min(input1[input1_partition], input2[input2_partition])
      
      print(max_of_left, min_of_right)
      return (max_of_left + min_of_right) / 2.0

input1 = [2]
input2 = [1,3]
print(median(input1, input2))
