def decimalToBinary(testVariable) :
  # Base Case
  if testVariable <= 1:
    return str(testVariable)

  # Recursive Case
  else:
    return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2) 
    # Floor division - 
    # division that results into whole number adjusted to the left in the number line

# Driver Code
testVariable = 20
print(decimalToBinary(testVariable))
