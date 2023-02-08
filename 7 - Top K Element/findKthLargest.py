import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
        
# Official solution

from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        minHeap = []

        for i in range(k):
            heappush(minHeap, nums[i])

        for i in range(k, len(nums)):
            if minHeap[0] < nums[i]:
                heappop(minHeap)
                heappush(minHeap, nums[i])

        return minHeap[0]
