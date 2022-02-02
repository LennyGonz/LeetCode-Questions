'''
LeetCode #347

Given an unsorted array of numbers, find the top 'K' frequently occurring numbers in it.

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

we need to find the most frequently occurring number compared to finding the largest numbers.

We can follow the same approach as discussed in the Top K Elements problem.

However, in this problem, we first need to know the frequency of each number, for which we can use a HashMap. 

Once we have the frequency map, we can use a Min Heap to find the 'K' most frequently occurring number. 

In the Min Heap, instead of comparing numbers we will compare their frequencies in order to get frequently occurring numbers
'''
from heapq import *

def find_k_frequent_numbers2(nums, k):
  # our result list
  topFrequentNumbers = []
  
  freqMap = {}
  
  # first we create the frequency map
  for num in nums:
    if num not in freqMap:
      freqMap[num] = 0
    freqMap[num] += 1
  
  # then we create the maxHeap
  # again we negate the value so the numbers that occur the most are at the top of the heap
  maxHeap = [(-val, key) for key,val in freqMap.items()]
  heapify(maxHeap)
  
  # we iterate from 0 to k
  # popping the root - k times
  # because the smallest number is the root (since we negated the values in reality, the smallest number is the largest)
  # but we don't care about the frequency value, we care about the number
  # so we append each number to our result list: topFrequentNumbers
  for _ in range(k):
    topFrequentNumbers.append(heappop(maxHeap)[1])
  
  return topFrequentNumbers
# -------------------------------------------------------------------- #
from collections import Counter

def find_k_frequent_numbers(nums, k):
  topFrequentNumbers = []
  
  frequency_map = Counter(nums)
  
  maxHeap = [(-val, key) for key,val in frequency_map.items()]
  
  heapify(maxHeap)
  
  for _ in range(k):
    topFrequentNumbers.append(heappop(maxHeap)[1])

  return topFrequentNumbers

def main():

  print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))) # [11,12]

  print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2))) # [11, 3]

  print()
  
  print("Here are the K frequent numbers using method2: " + str(find_k_frequent_numbers2([1, 3, 5, 12, 11, 12, 11], 2))) # [11,12]

  print("Here are the K frequent numbers using method2: " + str(find_k_frequent_numbers2([5, 12, 11, 3, 11], 2))) # [11, 3]

main()
