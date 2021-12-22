from heapq import *
'''
Given an unsorted array of numbers, find the 'K' largest numbers in it

ex1) Input: [3,1,5,12,2,11] & K = 3
Output: [5,12,11]
'''

def find_k_largest_numbers(nums, k):
  minHeap = []
  
  for i in range(k):
    heappush(minHeap, nums[i])
  
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])
  
  return list(minHeap)

'''
heapreplace: 
'''
def find_k_largest_numbers_2(nums, k):
  minHeap = []
  
  for i in range(k):
    heappush(minHeap, nums[i])
  
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heapreplace(minHeap, nums[i])
  
  return list(minHeap)

'''
1. We insert 'k' elements in the min-heap
2. After the insertion, the heap will have three numbers [3,1,5] with '1' being the root as it is the smallest element
3. We iteratre through the remaining numbers and perform if we encounter a larger number than our root we:
  - Take out the smallest number from the heap(the root)
  - Insert the larget number into the heap
4. Repeat step 3 for the remainder of the input array
5. return the minHeap (as a list) bc it has the 'k' largest numbers

It takes O(logK) to extract the minimum number from the min-heap.
So the overall time complexity is: O(K*logK + (N-K)*logK) since, first we insert 'K' numbers in the heap and then iterate through the remaining numbers and at every step, in the worst case, we need to extract the minimum number and insert a new number in the heap. This algorithm is better than O(N*logN)
'''

def main():

  print("Here are the top K numbers: " + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
  print("Here are the top K numbers: " + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))
  
  print()
  
  print("Here are the top K numbers using method2: " + str(find_k_largest_numbers_2([3, 1, 5, 12, 2, 11], 3)))
  print("Here are the top K numbers using method2: " + str(find_k_largest_numbers_2([5, 12, 11, -1, 12], 3)))

main()

'''
As discussed above, the time complexity of this algorithm is: O(K*logK + (N-K)*logK), which is asymptotically equal to O(N*logK)

Time: O(N*logK) - we iterate through all of the nums array(N) * heappop&heappush take logN time - but we only have K elements in the heap so logK -> N * logk

Space: The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
'''
