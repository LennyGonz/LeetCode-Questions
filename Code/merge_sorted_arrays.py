def mergeSortedArrays(nums1, m, nums2, n):
  pointer1 = m - 1
  pointer2 = n - 2

  for pointer in range(m+n-1, -1, -1):
    if pointer2 < 0:
      break
      
    if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
      nums1[pointer] = nums1[pointer1]
      pointer1 -= 1
    
    else:
      nums2[pointer] = nums2[pointer2]
      pointer2 -= 1
