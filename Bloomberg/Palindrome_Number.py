'''
LeetCode #9

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Brute-Force:
  - of course the first solution that comes to mind is casting the original output
    and comparing the original to a reversed version of the original
      - if they're the same (True) otherwise (False)

Without casting:
We rebuild the number in reverse

using an variable initialized to 0
We chop off the last digit in the input number
and make it the first digit in the reversed input number

We basically repeat this process and compare the original input and reversed number

1221 -> chop off the last digit (1)
0 (reversed_num) -> add chopped off number -> 1

122 -> chop off the last digit (2)
1 (reversed_num) -> add chopped off number -> 12

12 -> chop off the last digit (2)
12 (reversed_num) -> add chopped off number -> 122

1 -> chop off the last digit (1)
122 (reversed_num) -> add chopped off number -> 1221

1221 (original) == 1221 (reversed_num) #True

Optimized:

Through that example I noticed that if a number is a palindrome then - we really only need to compare half the number

So, instead of reversing the whole integer, let's build half of the reversed integer and then check if it's palindrome.

But we don't know when is that half going to come.

Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

x = 1595, revX = 1
x = 159, revX = 15
x = 15, revX = 159

We see that revX > x after 3 loops and we crossed the half way in the integer bc it's an odd length integer.
If it's an even length integer, our loop stops exactly in the middle.

Now we can compare x and revX, if even length, or x and revX//10 if odd length and return True if they match.
'''
# rebuild the entire number
# O(N) -> this can be improved to -> O(logN)
def isPalindrome(x):
  # if x is negative, return False
  # if x is positive and last digit is 0, that also cannot form a palindrome, return False.
  if x < 0 or (x >0 and x%10 == 0):
    return False

  # we need a copy of the input to create a reversed number
  # and since integers are not immutable, the copy is necessary
  num = x
  
  # this is what we'll use to create the number
  reversed_num = 0
  
  # while there is number
  while num > 0:
    # we want to chop off the last digit
    last_digit = num % 10
    
    # as we chop off each integer from the end of num
    # we'll need to place that chopped off integer in the correct place, so
    # we multiply the current reversed number by 10 and add the current chopped off integer
    reversed_num = (reversed_num * 10) + last_digit
    
    # so avoid an endless loop, our copy of the input integer must eventually be zero
    # so we update it by doing integer division of 10
    # which will get rid of the number we chopped off at the beginning
    num = int(num / 10)
  
  # once we're done iterating over the number -> we check to see if its a palindrome
  return reversed_num == x
'''
Time: O(N) - N being all the digits in the given number
Space: O(1) - algorithm runs in constant space
'''

# rebuild half the number -> O(logN)
def isPalindrome2(x):
  # if x is negative, return False
  # if x is positive and last digit is 0, that also cannot form a palindrome, return False.
  if x < 0 or (x > 0 and x % 10 == 0):
    return False
  
  # we use this to build half of the reversed integer
  revX = 0
  
  # we don't know what index is that halfway point so
  # we stop when result is greater than the original 
  # this will be when result reaches exactly the middle (even length number)
  # or when result crosses the halfway point (odd length number)
  while x > revX:
    last_digit = x % 10
    
    revX = (revX * 10) + last_digit
    
    x = x // 10
  
  return x == revX or x == revX // 10
'''
Time: O(logN) - we only iterate half the length of N
Space: O(1) - algorithm runs in constant space
'''

def main():
  print(isPalindrome(123))
  print(isPalindrome2(123))
  print()
  print(isPalindrome(122221))
  print(isPalindrome2(122221))

main()
