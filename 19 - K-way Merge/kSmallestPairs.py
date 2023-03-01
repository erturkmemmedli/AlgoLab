from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        heap = []

        for i in range(len(nums1)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        while k and heap:
            summ, row, col = heappop(heap)
            result.append((nums1[row], nums2[col]))
            k -= 1

            if col + 1 < len(nums2):
                heappush(heap, (nums1[row] + nums2[col + 1], row, col + 1))
            
        return result
      
# Official solution

from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []

        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
            
        output = []
        
        while k > 0 and heap:
            currentSum, n1, n2, index = heappop(heap)
            output.append((n1, n2))
        
            if index + 1 < len(nums2):
                heappush(heap, (n1+nums2[index+1], n1, nums2[index+1], index+1))
        
            k -= 1
                
        return output
