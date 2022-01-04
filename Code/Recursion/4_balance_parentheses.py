'''
Implement a function that takes an array testVariable containing opening ( and closing parenthesis ) and determines whether or not the brackets in the array are balanced. 

The function also takes startIndex = 0 and currentIndex = 0 as parameters.

What does “Balanced Parenthesis” Mean?
Balanced parentheses mean that each opening bracket ( has a corresponding closing bracket ). Also, the pairs of parentheses are properly nested.

Consider the following correctly balanced parentheses:
- ()
- (())
- (())()
- ((())) ((()))

Now take a look at some incorrectly balanced parentheses:
- (
- )()(
- ((()()()()
- ((())))((((()
'''

def balanced(testVariable, startIndex = 0, currentIndex = 0) :
  if currentIndex == len(testVariable):
    return startIndex == 0
  
  if startIndex < 0:
    return False
  
  if testVariable[currentIndex] == '(':
    return balanced(testVariable, startIndex+1, currentIndex+1)
  elif testVariable[currentIndex] == ')':
    return balanced(testVariable, startIndex-1, currentIndex+1)

example1 = "((()))()"
print(balanced(example1))

def balanced_iterative(brackets):
  check = 0
  for bracket in brackets:
    if bracket == '(':
      check += 1

    elif bracket == ')':
      check -= 1

    if check < 0:
      break

  return check == 0

print(balanced_iterative(example1))
