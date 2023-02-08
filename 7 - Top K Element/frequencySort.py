import heapq
import collections

class Solution:
    def frequencySort(self, nums):
        counter = collections.Counter(nums)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (v, -k))
        sortedArray = []
        for _ in range(len(heap)):
            count, num = heapq.heappop(heap)
            for i in range(count):
                sortedArray.append(-num)
        return sortedArray
      
# Official solution

from heapq import *
class Solution:
    def frequencySort(self, nums):
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        minheap = []

        for num, frequency in freq.items():
            heappush(minheap, (frequency, -num))

        output = []

        while minheap:
            frequency, num = heappop(minheap)

            for i in range(frequency):
                output.append(-num)

        return output
