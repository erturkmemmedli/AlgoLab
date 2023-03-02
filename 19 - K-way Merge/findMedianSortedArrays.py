from heapq import *

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total_length = len(nums1) + len(nums2)
        k = total_length // 2

        if not nums1:
            return nums2[k] if total_length & 1 else (nums2[k-1] + nums2[k]) / 2
        if not nums2:
            return nums1[k] if total_length & 1 else (nums1[k-1] + nums1[k]) / 2

        heap = []
        heappush(heap, (nums1[0], 1, 0))
        heappush(heap, (nums2[0], 2, 0))

        while k:
            val, arr_no, idx = heappop(heap)
            k -= 1

            if arr_no == 1 and idx + 1 < len(nums1):
                heappush(heap, (nums1[idx + 1], arr_no, idx + 1))
            if arr_no == 2 and idx + 1 < len(nums2):
                heappush(heap, (nums2[idx + 1], arr_no, idx + 1))
        
        return heap[0][0] if total_length & 1 else (val + heap[0][0]) / 2
        
# Official solution

from heapq import *

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = 2
        i = [0] * k
        n = [len(nums1), len(nums2)]
        array = [nums1, nums2]
        heap = []
        
        for j in range(k):
            if i[j] < n[j]:
                heappush(heap, (array[j][i[j]], j))
                i[j] += 1
                
        result = []
        
        while len(result) < (n[0] + n[1]):
            val, j = heappop(heap)

            result.append(val)
            
            if i[j] < n[j]:
                heappush(heap, (array[j][i[j]], j))
                i[j] += 1
        
        if (n[0] + n[1]) % 2 == 0:
            return (result[-2] + result[-1]) / 2

        return result[-1]
