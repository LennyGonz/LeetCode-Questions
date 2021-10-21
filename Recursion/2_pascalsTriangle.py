def printPascal(n):
  if n == 0:
    return [1]
  
  else:
    # initialize the line with the leading 1
    line = [1]

    # recursive call till we reach the base call
    previousLine = printPascal(n-1)

    # len(previousLine) - 1 = this means we traverse all elements in the array without going out of bounds
    # with that range limit we are allowed to correctly do previousLine[i] + previousLine[i+1] without going out of bounds
    # remember we need to do the sum of the 2 numbers above it to find the corresponding number
    for i in range(len(previousLine)-1):
      line.append(previousLine[i] + previousLine[i+1])
      
    # add trailing one
    line += [1]
  return line

print(printPascal(5)) # [1, 5, 10, 10, 5, 1]
