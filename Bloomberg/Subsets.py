'''
LeetCode #78

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

-------------------------------------------------------------------------------------------------

To generate all subsets of the given set, we can use a BFS approach
We can start with an empty set, iterate through all the elements one-by-one, and add them to existing sets to create a new subset

ex) Given set [1,5,3]

1. start with an empty set: [[]]
2. add the first number(1) to all the existing subsets to create a new subsets: [[],[1]]
3. add the second number(5) to all the existing subsets: [[],[1],[5],[1,5]]
4. Add the third number(3) to all the existing subsets: [[],[1],[5],[1,5],[3],[1,3],[5,3],[1,5,3]]

                        []
                      /     \
                    copy    add 1
                    /         \
                  []          [1]
                  /             \
                copy            add 5
                /                 \
            [], [1]             [5], [1,5]
            /                       \
          copy                    add 3
          /
[], [1], [5], [1,5]             [3],[1,3],[5,3],[1,5,3] -> result = [[],[1],[5],[1,5],[3],[1,3],[5,3],[1,5,3]]

Time: O(N * 2^N) - since in each step the number of subset doubles, since we're adding each element to th all the existing subsets we have a runtime of O(2^N)
                    - where N is the total number of elements in the input set
                    - and since we're constructing a subset from an existing set we add the O(N) -> O(N * 2^N)

Space: O(N * 2^N) - We have a total of 2^N subsets multiplied by the number of elements in the inputset: N -> therefore O(N * 2^N)
'''
def find_subsets(nums):
  result = []
  
  # start by adding the empty subset
  result.append([])
  
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    for i in range(len(result)):
      
      # create a new subset from the existing subset 
      set1 = list(result[i])
      
      # and insert the current element to it
      set1.append(currentNumber)
      
      # add the new subset to our result list
      result.append(set1)

  return result

def main():
  print("Here is the list of subsets: " + str(find_subsets([1, 2, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
  print("Here is the list of subsets: " + str(find_subsets("abc")))

main()
