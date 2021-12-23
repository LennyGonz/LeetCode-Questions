def counting_sort(array, digit, base=10):
  counts = [[] for _ in range(base)]

  for num in array:
    d = (num // base ** digit) % base
    counts[d].append(num)

  result = []
  for bucket in counts:
    result.extend(bucket)

  return result

def radix_sort(array, digits=10):
  for digit in range(digits):
    array = counting_sort(array, digit)

  return array

'''
Counting sort takes O(N + M), where M is the maximum bucket size. 
For our problem, we can consider this to be O(N). We must perform this sort k times, where k is the number of digits in the maximum number, in this case 10. 
The time complexity of this algorithm is therefore O(10 * N), or if we treat k as constant, O(N).
'''
