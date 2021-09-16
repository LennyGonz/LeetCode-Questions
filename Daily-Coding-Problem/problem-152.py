from random import random
from bisect import bisect_left

def preprocess(probs):
  lst = []

  current_val = 0
  for p in probs:
    current_val += p
    lst.append(current_val)

  return lst

def distribute(nums, arr):
  r = random()
  i = bisect_left(arr, r)
  return nums[i]
