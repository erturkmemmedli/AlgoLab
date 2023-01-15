class Solution:
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        while left + 2 <= right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                left = mid
            else:
                right = mid
                
# Official solution

class Solution(object):
    def peakIndexInMountainArray(self, A):
        start = 0
        end = len(A) - 1
        while start < end:
            middle = start + (end - start) // 2
            if A[middle] < A[middle + 1]:
                start = middle + 1
            else:
                end = middle
        return start
