def apply_ops(ops, values):
  op = ops.pop()
  right, left = values.pop(), values.pop()
  if op == '+':
    values.append(left + right)
  else:
    values.append(left - right)

def parse(equation):
  values = []
  ops = []

  for char in equation:
    if char.isdigit():
      values.append(int(char))
    elif char == '(':
      ops.append(char)
    elif char == ')':
      while ops and ops[-1] != '(':
        apply_ops(ops, values)
      ops.pop()
    elif char == ' ':
      continue
    else:
      while ops and ops[-1] not in "()":
        apply_ops(ops, values)
      ops.append(char)

  while ops:
      apply_ops(ops, values)

  return values[0]

def fix_negatives(equation):
  if equation[0] == '-':
    equation = '0' + equation

  equation = equation.replace('(-', '(0-')

  return equation
