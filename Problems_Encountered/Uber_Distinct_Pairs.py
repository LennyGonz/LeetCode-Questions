'''
I want a sliding window sort of approach
I start at the first element move to the right
then move the second element move to the right
then move the third element move to the right
etc until not possible anymore
'''
def almostEqualNumbers(numbers):
  s_num = []

  for x in numbers:
    s_num.append(str(x))
  
  print(s_num)
  res = set()

  # for num in s_num:
  #   for other_num in range(1, len(s_num)):
  #     print("num: ", num, " other_num: ", s_num[other_num])
  #     if num != s_num[other_num] and len(num) == len(s_num[other_num]):
  #       res.add((num, s_num[other_num]))
  #     else:
  #       continue

  window_start = 0

  while window_start < len(s_num):
    print(s_num[window_start])
    window_start += 1

  
  print(res)
  
ex1 = [1, 151, 241, 1, 9, 22, 351]
print(almostEqualNumbers(ex1))

'''
We can do this in 1 pass... im just not sure how
'''
