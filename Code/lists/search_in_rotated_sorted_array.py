'''
LeetCode #33 - Search in Rotated Sorted Array

Suppose an array sorted in ascending order is roated at some pivot UNKNOWN to you beforehand

(i.e., [0,1,2,4,5,6,7] MIGHT become [4,5,6,7,0,1,2])

You are given a target value to search.
If found in the array RETURN its index
IF NOT found return -1

You MAY ASSUME no duplicates exist in the array

Your algorithm's runtime complexity MUST be O(log N)

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

------------------------------------------------------------------------------------------------

So brute-force 

We could immediately just search through the array for the target and we can do this in O(N) time

However, if we really "think" about it - we can do this in O(log N) time using binary search

Now since the sorted input array has been rotated, MEANING some of the larger numbers have been moved to the front

This creates distinct scenarios

If the target > middle value -> we eliminate all the values to the left of middle and search all values to the right of middle

However, if target < middle (ex: [4,5,6,7,0,1,2] where middle = 7 & target = 0)
Then we have 2 portions of the array where our target can be [4,5,6] or [0,1,2]

In order to decide which portion we run binary search on - we use the left most value - in this example that's 4
  if target < left most value -> we run binary search on [0,1,2]
  if target >= left most value -> we run binary search on [4,5]

Think about it - left side of the array has larger numbers SO if target > left-most-value - we want to search on the right side, where the smaller numbers are

SO we search the right portion of the sorted array on 2 conditions:

1) target > middle value
2) target < left most value

We search the left portion of the sorted array if:

* target >= left most value (THIS also makes sense, bc the left side has the greater numbers, the left most value is the smallest of the larger numbers)

^ these conditions are true WHEN we find ourslves in the left side of the array

IF we are on the right side of the array:

We search the left portion of the sorted array on 2 conditions:

1) target < middle value
2) target > right most value

Again the right side has the lower value numbers, so the right most value is the largest of the lower value numbers
  -> therefore if target is greater than the right most value -> it makes sense to search the left most side of the array where all the largest numbers were rotated to

We search the right side IF:
* target > middle AND targer <= right most value

NOW the last thing to determine is - how do we know if we're on the left or right side of the input sorted array
Im going to decide that based on:

if middle value > left value -> the middle value belongs to the left sorted portion
otherwise -> belongs to the right sorted portion
'''

def search(nums, target):
  # we need to initialize our pointers
  left, right = 0, len(nums)-1
  
  # our condition for looping is - while left is less than or equal to right - if they cross each other we stop
  # also we need them to be equal because if we have a single value array - ex: [1] - we still need to check that value
  while left <= right:
    # we need to compute middle each time we reduce our search parameter
    middle = (left + right) // 2
    
    # if the target is in the array - here is where we'll catch it
    # we'll reduce our window until middle is at the index of target
    if target == nums[middle]:
      return middle
    
    # we need to check which portion of the array we're in
    # left sorted portion
    if nums[middle] >= nums[left]:
      # if we're in the left sorted portion of the array - there are 2 conditions where we eliminate every element to the left of middle
      # And therefore we move our search to the RIGHT sorted portion of the input array
      if target > nums[middle] or target < nums[left]:
        # therefore, we need to adjust the left pointer
        left = middle + 1

      # the target is less than the middle BUT greater than the left most value
      # that means we search the left portion SO we have to update our right pointer
      else:
        right = middle - 1

    # if we're not in the left sorted portion - then we're in the right sorted portion
    else:
      # if we're in the right sorted portion of the array - there are 2 conditions where we eliminate every element to the right of middle
      # And therefore we move our search to the left sorted portion of the input array
      if target < nums[middle] or target > nums[right]:
        # since we're going left we have to update our right pointer
        right = middle - 1
        
      # the target is greater than the middle BUT less than the right most value
      # that means we search the right portion SO we have to update our left pointer
      else:
        left = middle + 1
  
  # if we find our target it'll be caught in the beginning and we return middle
  # so if we DONT find it AND we exit the loop and return -1
  
  return -1

'''
Time: O(log n) - we reduce our search by half the elements at each iteration
Space: O(1) - the algorithm runs in constant space

ex: [4,5,6,7,0,1,2] Target = 0

Our target is 0

0 is less than 7 -> we could be looking at [4,5,6] or [0,1,2]

We start by looking at the left portion bc our middle value (7) belongs to the left
Is target less than our left most value (4)  - yes

So we can eliminate everything to the left of our middle value (including the middle value)
So we're left with [0,1,2]

Our new left points to 0
and new mid points to 1

Are we in the left sorted or right sorted portion

Since 1 is greater than or equal to 0 - we're saying that 1 belongs to the left portion
So now we compare middle to target

Target is less than middle so now we go left
if we compare target to the left most value - our target is greater than or equal to it and we go left

[0]

we're left with [0] and we can return the index of it: 4
'''

def main():
  print(search([4,5,6,7,0,1,2], 0)) # should return 4
  print(search([4,5,6,7,0,1,2], 3)) # should return -1 bc 3 is not in the array
  print(search([1], 0)) # should return -1 bc 0 is not in the array
  print(search([1], 1)) # should return 0

main()


