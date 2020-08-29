def twoSum(numarr, target):
  processedInts = {}

  for index, value in enumerate(numarr):
    if target - value in processedInts:
      return [processedInts[target-value], index]
    else:
      processedInts[value] = index
    
  return 0

ex1 = [2, 7, 11, 15]
print(twoSum(ex1, 26))
