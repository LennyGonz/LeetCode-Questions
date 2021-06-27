class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getVal(arr, i):
            if i == -1:
                return float("-inf")
            if i == len(arr):
                return float("inf")
            
            return arr[i]
  
        def getIndices(rightShort, shortArray, longArray):
            midIndex = (len(shortArray) + len(longArray)) / 2
            rightLong = midIndex - rightShort
            return(rightShort - 1, rightShort, rightLong - 1, rightLong)
        
        def getDirection(leftShort, rightShort, leftLong, rightLong, shortArray, longArray):
            if getVal(shortArray, leftShort) > getVal(longArray, rightLong):
                return -1
            
            elif getVal(longArray, leftLong) > getVal(shortArray, rightShort):
                return 1
            
            else:
                return 0
            
        def getResult(leftShort, rightShort, leftLong, rightLong, shortArray, longArray):
            odd = (len(shortArray) + len(longArray)) % 2
            
            if odd:
                return min(getVal(longArray, rightLong), getVal(shortArray, rightShort))
            
            else:
                return (max(getVal(shortArray, leftShort), getVal(longArray, leftLong)) + min(getVal(shortArray, rightShort), getVal(longArray, rightLong))) / 2.0
        
        shortArray = nums1
        longArray = nums2
        
        if len(nums1) > len(nums2):
            shortArray = nums2
            longArray = nums1
        
        leftShort = rightShort = leftLong = rightLong = direction = 1
        
        left = 0
        right = len(shortArray)
        
        while direction != 0:
            midpoint = (left + right) / 2
            
            leftShort, rightShort, leftLong, rightLong = getIndices(midpoint, shortArray, longArray)
            
            direction = getDirection(leftShort, rightShort, leftLong, rightLong, shortArray, longArray)
            
            if direction < 0:
                right = midpoint - 1
                
            elif direction > 0:
                left = midpoint + 1
        
        return getResult(leftShort, rightShort, leftLong, rightLong, shortArray, longArray)
