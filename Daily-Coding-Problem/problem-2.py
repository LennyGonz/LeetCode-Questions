def get_factors(array):

  result = list()
  cumulativeProduct = 1

  for num in array:
    cumulativeProduct *= num

  for num in array:
    temp = cumulativeProduct // num
    result.append(temp)
  
  return result

print(get_factors([1,2,3,4,5]))

## No division answer below

def multiplyArray(numlist):
  right_prod_array = list()
  cumulative_product = 1
  for num in numlist:
    cumulative_product *= num
    right_prod_array.append(cumulative_product)
  
  cumulative_product = 1
  left_prod_array = list()
  for num in numlist[::-1]:
    cumulative_product *= num
    left_prod_array.append(cumulative_product)

  left_prod_array = left_prod_array[::-1]

  output_array = list()

  for i in range(len(numlist)):
    num = None

    if i == 0:
      num = left_prod_array[i + 1]
    
    elif i == len(numlist) - 1:
      num = right_prod_array[i - 1]
    
    else:
      num = right_prod_array[i - 1] * left_prod_array[i + 1]

    output_array.append(num)
  
  return output_array

print(multiplyArray([1,2,3,4,5]))
