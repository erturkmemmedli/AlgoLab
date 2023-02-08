from heapq import heappop, heappush
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        for key, val in counter.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                if val > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (val, key))
        return [k for _, k in heap]
      
# Official solution

from heapq import*
class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 0

            freq[num] += 1
            
        minHeap = []

        for element, frequency in freq.items():
            heappush(minHeap, (frequency, element))

            if len(minHeap) > k:
                heappop(minHeap)
        
        output = []

        while minHeap:
            output.append(heappop(minHeap)[1])
        
        return output
