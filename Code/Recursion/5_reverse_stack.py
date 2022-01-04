import stack as s
'''
Implement a function that takes a stack, testVariable, and reverses it. Do not use any other extra stack or data structure.

Input: [8, 5, 3, 2]
Output: [2, 3, 5, 8]
'''

# Recursive function that inserts an element at the bottom of a stack.
def insertAtBottom(stack, item):
  # Base case
  if s.isEmpty(stack) :
    s.push(stack, item)

  # Recursive case
  # Similar to the main function -> we empty out our stack to place in order to place the element at the top
  else:
    temp = s.pop(stack) # we pop whatever was in there and we hold it
    insertAtBottom(stack, item) # recursively empty out the stack, till we hit our base case
    s.push(stack, temp) # once the recursive calls absolve, we start appending the elements to the back
    # push is actually append, so the elements that were on the stack previously are appending to the back

def reverse(stack) :
  # Recursive case
  if not s.isEmpty(stack) :
    temp = s.pop(stack) # holding the last element of the stack, so once the recursive calls get absolved 
    # what used to be the last element will be at the top
    reverse(stack) # We are recursively emptying out our stack 
    insertAtBottom(stack, temp) # this recursive call will start to build our new reversed stack

# Driver Code 
myStack = s.createStack() 
s.push(myStack, str(8)) 
s.push(myStack, str(5)) 
s.push(myStack, str(3)) 
s.push(myStack, str(2)) 

print("Original Stack") 
s.printStack(myStack) 

reverse(myStack) 

print("\n\nReversed Stack") 
s.printStack(myStack) 
print()

'''
def insert_at_bottom(stack, element):
  if len(stack) == 0:
    stack.append(element)
  else:
    temp = stack.pop() # 2
    insert_at_bottom(stack, element) # [] , 3
    stack.append(element) # [3].append(2) -> [3,2] -> [5].append(3) -> [5,3].append(2) -> [5,3,2] -> [8].append(5) -> [8,5].append(3) -> [8,5,3].append(2) -

def reverse_stack(stack):
  if len(stack) != 0:
    last_item = stack.pop()
    reverse_stack(stack)
    # we'll reach insert_at_bottom once we've popped all the elements (ignoring the fact that it'll get called 1 more time after the last element)
    # our helper function -> insert_at_bottom will take our currently empty stack, and the last item of the stack
    insert_at_bottom(stack, temp)
  
  return stack

ex1 = [2,3,5,8]
print(reverse_stack(ex1)) # [8,5,3,2]
'''
