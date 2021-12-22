'''
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
'''

from heapq import *
from collections import Counter

def find_k_frequent_numbers(nums, k):
  topFrequentNumbers = []
  
  frequency_map = Counter(nums)
  
  maxHeap = [(-val, key) for key,val in frequency_map.items()]
  
  heapify(maxHeap)
  
  for _ in range(k):
    topFrequentNumbers.append(heappop(maxHeap)[1])

  return topFrequentNumbers

def find_k_frequent_numbers2(nums, k):
  topFrequentNumbers = []
  
  freqMap = {}
  
  for num in nums:
    if num not in freqMap:
      freqMap[num] = 0
    freqMap[num] += 1
  
  maxHeap = [(-val, key) for key,val in freqMap.items()]
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
