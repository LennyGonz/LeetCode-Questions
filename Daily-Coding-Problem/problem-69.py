from math import inf

def maximum_product_of_three(lst):
  max1, max2, max3, min1, min2 = -inf, -inf, -inf, inf, inf

  for x in lst:
    if x > max1:
      max3 = max2
      max2 = max1
      max1 = x
    elif x > max2:
      max3 = max2
      max2 = x
    elif x > max3:
      max3 = x

    if x < min1:
      min2 = min1
      min1 = x
    elif x < min2:
      min2 = x

  return max(max1 * max2 * max3, max1 * min1 * min2)
