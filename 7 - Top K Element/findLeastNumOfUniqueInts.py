import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
        while k > 0 and heap:
            count, _ = heapq.heappop(heap)
            k -= count
        return len(heap) if k >= 0 else len(heap) + 1
        
# Official solution

from heapq import *
import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        arr_count = collections.Counter(arr)
        heap = []

        for num, count in arr_count.items():
            heappush(heap, (count, num))
        
        while k:
            count, num = heappop(heap)
            count -= 1
            
            if count > 0:
                heappush(heap, (count, num))
                
            k -= 1

        return len(heap)
