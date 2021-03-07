def twosum(list, target):
  processed_digits = []
  for num in list:

    if target-num in processed_digits:
      return True
    else:
      processed_digits.append(num)
  
  return False

numlist = [10, 15, 3, 7]
numtarget = 17
print(twosum(numlist, numtarget))
