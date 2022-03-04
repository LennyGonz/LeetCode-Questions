'''
LeetCode #150

1. We iterate through the list (ask if the list elements are strings) or if the input is even a list (could be a string)

2. As we traverse the input, each time we reach an operator we replace the value at the operator index AND
    the 2 numbers before with the value of 2 operands with the operation applied (i.e [2, 3, +] -> [5])

Quick Recap:
1. so visit each element in linear order
2. get 2 of the most recently seen numbers that haven't yet been replaced (we keep track of this using a stack), apply the operator, push back into a stack

IF THE INPUT IS A STRING - ANSWER BELOW
'''

def evalRPN(tokens):
  # we use the stack to hold the summation values whenever we reach a operator
  stack = []
  
  # iterate over the input array: Tokens
  for token in tokens:
    
    # while we iterate through tokens
    # if the current element is NOT an operator add it to the stack
    if token not in "+-/*":
      stack.append(int(token))
      # we terminate the current iteration - we do that with *continue* so the rest of the code isnt executed
      continue
    
    # if the current element is NOT an operand
    # then we have an operator and must pop off the latest 2 numbers
    number2 = stack.pop()
    number1 = stack.pop()
    
    # we need something to hold the result of the operator
    result = 0
    
    # depending on which the operator the current token is we perform the action
    if token == "+":
      result = number1 + number2
    elif token == "-":
      result = number1 - number2
    elif token == "/":
      result = int(number1 / number2) # in python this is how we do integer division
    else:
      result = number1 * number2
    
    stack.append(result)
  
  # when we finish iterating over the inputArray: tokens
  # result will hold the end result
  # therefore we return it
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
  
  # depending on how the string looks we split the string based on the delimiter
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
