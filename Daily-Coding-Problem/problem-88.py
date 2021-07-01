def divide(x, y):
  if y == 0:
    raise ZeroDivisionError('division by zero')

  quotient = 0
  power = 32           # Assume 32-bit integer
  yPower = y << power  # Initial y^d value is y^32
  remainder = x        # Initial remainder is x
  while remainder >= y:
    while yPower > remainder:
      yPower >>= 1
      power -= 1
    quotient += 1 << power
    remainder -= yPower

  return quotient
