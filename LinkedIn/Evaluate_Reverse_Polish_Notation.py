'''
We iterate through the list (ask if the list elements are strings) or if the input is even a list (could be a string)
As we traverse the input, each time we reach an operator we replace the value at the operator index AND the 2 numbers before with the value of 2 operands with the operation applied (i.e [2, 3, +] -> [5])

1. so visit each element in linear order
2. get 2 of the most recently seen numbers that haven't yet been replaced (we keep track of this using a stack), apply the operator, push back into a stack

IF THE INPUT IS A STRING - ANSWER BELOW
'''

def evalRPN(tokens):
  stack = []
  
  for token in tokens:
    if token not in "+-/*":
      stack.append(int(token))
      continue
      
    number2 = stack.pop()
    number1 = stack.pop()
    
    result = 0
    
    if token == "+":
      result = number1 + number2
    elif token == "-":
      result = number1 - number2
    elif token == "/":
      result = int(number1 / number2) # in python this is how we do integer division
    else:
      result = number1 * number2
    
    stack.append(result)
  
  return result

'''
Time: O(N) - we did this in 1-pass & N is the total number of elements in the list
Space: O(N) - we use a stack, and not even in worst case do we push all N elements, bc operators dont get pushed
'''

def evaluate(RPN_EXPRESSION):
  stack = []
  delimiter = ','
  operators = {
    '+': lambda y, x: x + y,
    '-': lambda y, x: x - y,
    '*': lambda y, x: x * y,
    '/': lambda y, x: int(x / y)
  }
  
  for token in RPN_EXPRESSION.split(delimiter):
    if token in operators:
      stack.append(operators[token](stack.pop(), stack.pop()))
    
    # else token is a number
    else:
      stack.append(int(token))

  return stack[-1]

'''
Time: O(N)
Space: O(N)
'''
