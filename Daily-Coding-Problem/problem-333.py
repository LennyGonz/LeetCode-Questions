'''
At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 

To help figure out who this is, you have ACCESS to an O(1) method called: knows(a, b), 

which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

---------------------------------------------------------------------------------------------------------------------

We can implement this more efficiently by using a stack.

Note that for any call to knows, we can eliminate one of the two people from contention.

If 'i' knows 'j', it is impossible for 'i' to be the celebrity, since the celebrity does not know anyone.
On the other hand, if 'i' does not know 'j', 'j' cannot be the celebrity.

Following this logic, we continue popping two people from our input list and putting one back, until 
we have reduced our list down to a single person, who must be the celebrity.
'''
def find_celebrity(people):
  while len(people) > 1:
    i, j = people.pop(), people.pop()

    # the function: knows is given to us
    if knows(i, j):
      people.append(j)
    else:
      people.append(i)

  return people[0]

'''
This approach will require N calls to knows, and no additional space besides the input array, so it will run in O(N) time and O(1) space.
'''
