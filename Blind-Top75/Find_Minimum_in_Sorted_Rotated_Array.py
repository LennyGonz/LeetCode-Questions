'''
Leetcode #153

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Brute-Force: Obviously we can just iterate through the list, keeping track of a minimum so far -> gives us linear time O(N)

In log(N) time, the input is SORTED, which means they're suggesting we use Binary Search

Now remember the array is rotated, which means there are a certain amount of the largest numbers in the array
  that got moved to the very front of the list
  ex) Input: nums = [4,5,6,7,0,1,2] -> The original array was [0,1,2,4,5,6,7]

So if our middle pointer is currently pointing at value that belongs to the left sorted portion
  - we want to search the right sorted porition bc that's where the smaller values will be

if our middle pointer is at a value that belongs to the right sorted portion
  - then we want to search the left sorted portion, bc everything to the right is going to be greater

But then how do we determine which side middle belongs to ?
  - well if nums[mid] >= nums[left]
    - that means middle is pointing to a value greater than the smallest value of all the larger values
    - therefore middle belongs to the left portion
  
  - if nums[mid] !>= nums[left]
    - that means middle belongs to the right portion

So if we have: [3, 4, 5, 1, 2]
                ^     ^     ^
              left   middle right
            
            middle(5) >= left (3) therefore we're in the left portion of the sorted rotated array
            * remember wince the array is rotated, the smallest numbers were shifted to the right side

* So if our middle pointer is currently pointing at a value that belongs to the left sorted portion
  * we want to search the right sorted portion BECAUSE
    * the right sorted portion has the smaller values

* If our middle pointer is at a value that belongs to the right sorted portion (1)
  * then we want to search to the left b/c everything to the right of Middle is going to be an element greater

We need to do nums[mid] >= nums[left] - b/c both pointers can be pointing at the same element
  * this is an edge case

* this algorithm only works for rotated arrays
* REMEMBER the objective is to find the MINIMUM element in the sorted rotated array
'''
def findMin(nums):
  res = nums[0]
  left = 0
  right = len(nums) - 1
  
  while left <= right:
    # for scenarios where the rotated array
    # is a correctly sorted array
    # i.e [1,2,3,4,5,6]
    if nums[left] < nums[right]:
      res = min(res, nums[left])
      break
  
    # otherwise -> we begin binary search
    # set the midpoint
    mid = (left + right) // 2
    
    # update the value of res if necessary
    res = min(res, nums[mid])
    
    # if we're on the left portion -> search the right side
    if nums[mid] >= nums[left]:
      left = mid + 1
    
    # if we're on the right portion -> search the left side
    else:
      right = mid - 1
  
  return res

'''
Time: O(log N) - we constantly search half of the input list
Space: O(1) - algorithm runs in constant space
'''
