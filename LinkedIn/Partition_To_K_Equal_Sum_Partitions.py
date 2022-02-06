'''
LeetCode #698 - Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
---------------------------------------------------------------------------------------------------------------------------------------------------
Brute-Force:

1. Our goal is to break the given array into k subsets of equal sums.
    - Firstly, we will check if the array sum can be evenly divided into k parts by ensuring that totalArraySum % k is equal to 0.
    - If it can - then our targetSum is: totalArraySum / k

2. An intuitive way to approach this problem is to build each subset by randomly selecting one element at a time. 

3. Since the whole array has a sum of totalArraySum, then as long as the current subset's sum currentSubsetSum < (totalArraySum / k)
    - we can randomly select elements to add to the current subset.
    - If the currentSubsetSum becomes equal to (totalSum / k),
      - *then we have found one subset of the desired sum and we can proceed to make another subset.*
    - However, if the currentSubsetSum is greater than (totalSum / k), we need to go back and try to build this subset differently.
      - This can be done using a backtracking algorithm.

Why BackTracking?
- If we don't reach the desired solution, then we UNDO whatever we did when trying to solve that subproblem
    And then try to solve the subproblem again by making a different choice.

- So in this problem, we will pick one element and try including it in our subset, 
    - if after including this element in the current subset we can't make a valid combination of all subsets, then 
    - we will discard the last picked element, hence we will backtrack and try another element.
---------------------------------------------------------------------------------------------------------------------------------------------------
Optimal:

In order to optimize we can:

1. Sort the Array in Descending order
    - If we sort the array in ascending order (smaller values on the left side),
    - then there would be more recursion branches (recursive calls).
      - This is because when the change in subset-sum is small, more branches will be repeatedly created during the backtracking process.

1. To avoid using duplicate values in each subset we create a boolean array
  - whenever we find a values that create the targetValue - we mark all of them as True so we can't use them in the future

2. To create a subset whose sum is equal to targetSum
  - We start by iterating through the input array
    - each time we get to an integer... we have a decision
      - we can put this integer into a subset
      OR
      - we don't put the integer into the subset
  ** so we're making 2 decisions for every element in the input array (time wise this means => 2^n) **

So the idea is we're basically creating a decision tree for each element in the input array

More specifically we're creating k trees (because thats the number of subsets we want)
These trees will have a height of k*n, and will be stacked on top of each other -> due to our backtracking implementation
SO the overall time complexity will be 2^(k*n)

'''
def canPartition(nums, k):
  # if the sum of nums IS NOT divisible by K
  # meaning there is a remainder if we try to divide it by k
  # it'll be impossible to have K Equal Sum subsets
  if sum(nums) % k:
    return False
  
  # if we sort the input array in reverse order (biggest to smallest)
  # It will save a little but of time, b/c it'll make our base case execute a little faster
  # specifically here: subsetSum + nums[j] > target
  nums.sort(reverse=True)

  # we need to identify the targetSum - this will be the Equal sum in each subset
  target = sum(nums) / k
  
  # here we create the boolean array to keep track of the numbers we've used
  used = [False] * len(nums)
  
  def backTrack(index, k, subsetSum):
    # the problem asks to create K Equal Sum Subsets
    # Even if the input array has more integers - if we've created K Equal Sum Subsets
    # we can immediately return True
    if k == 0:
      return True
    
    # if the subsetSum == target
    # that means we've successfully created a subset with the targetSum
    # therefore we begin our search for a new subset
    # HOWEVER we reduce K by 1 -> because we've successfully found a subset whose sum == target
    if subsetSum == target:
      return backTrack(0, k-1, 0)
    
    # we use pointer j to iterate through all the values in the inputArray - starting at index i UNTIL the end of the array
    # And essentially while iterating through this array we'll be saying
    # we can EITHER choose it
    # OR
    # NOT choose it
    for j in range(index, len(nums)):
      # we only choose the value IF it's available
      # OR
      # if the current value will help our current subsetSum == target
      # if either of these conditions are violated then
      # we're going to continue to the next iteration of the loop skipping the current value (nums[j]) 
      if used[j] or subsetSum + nums[j] > target:
        continue
      
      # if value doesnt violate the conditions - its a valid value
      # so we need to mark it as True - so in future calculations we know if we can use it or not
      used[j] = True
      
      # instead of starting our search for each element to include from the 0th index, again and again
      # we can continue the search from the last picked element.
      # hence the j+1
      # we also update the value of subsetSum so we find the element that will help us reach targetSum
      if backTrack(j + 1, k, subsetSum+nums[j]):
        return True
      
      # After we've done the backtracking (we clean up)
      # we just reverse the decision - which is commonly done with backtracking (the undo portion)
      used[j] = False
    
    return False

  return backTrack(0, k, 0)

'''
Time Complexity: O(2^(k*N)) - For each element in the input array we either put the element in the subset or not (2^N). 
                                That means we're creating a decision tree - specifically we're creating k trees (because thats the number of subsets we want)
                                These trees will have a height of k*n, and will be stacked on top of each other -> due to our backtracking implementation
                                SO the overall time complexity will be O(2^(k*N))

Space Complexity: O(N) - Our boolean array is of size N to mark the already used elements (N).
                          And the recursive tree makes at most N calls at one time, so the recursive stack also takes O(N) space.
                          So O(N) + O(N) = O(2N) -> O(N)
'''

print(canPartition([4,3,2,3,5,2,1], 4)) # True
print(canPartition([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4], 7)) # False

print("----")

# SAME IDEA - SAME RUNTIME
# DIFFERENT IMPLEMENTATION
def canPartitionKSubsets(nums, k):
  nums_sum = sum(nums)
  if nums_sum % k != 0:
    return False
  subset_sum = nums_sum / k

  nums.sort(reverse=True)
  visited = [False] * len(nums)
  
  def can_partition(rest_k, cur_sum=0, next_index=0):
    if rest_k == 1:
      return True
    
    if cur_sum == subset_sum:
      return can_partition(rest_k - 1)
    
    for i in range(next_index, len(nums)):
      if not visited[i] and cur_sum + nums[i] <= subset_sum:
        visited[i] = True
        if can_partition(rest_k, cur_sum=cur_sum + nums[i], next_index=i + 1):
          return True
        visited[i] = False
    return False 
  
  return can_partition(k)

print(canPartitionKSubsets([4,3,2,3,5,2,1], 4)) # True
print(canPartitionKSubsets([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4], 7)) # False
