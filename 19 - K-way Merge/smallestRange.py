from heapq import *

class Solution:
    def smallestRange(self, nums):
        minHeap = []
        maxHeap = []

        for i in range(len(nums)):
            heappush(minHeap, (nums[i][0], i, 0))
            heappush(maxHeap, (-nums[i][0], i, 0))

        small, big = minHeap[0][0], -maxHeap[0][0]

        while True:
            root, row, col = heappop(minHeap)

            if col + 1 < len(nums[row]):
                heappush(minHeap, (nums[row][col + 1], row, col + 1))
                heappush(maxHeap, (-nums[row][col + 1], row, col + 1))
            else:
                break

            if -maxHeap[0][0] - minHeap[0][0] < big - small:
                small, big = minHeap[0][0], -maxHeap[0][0]

        return [small, big]
        
# Official solution

from heapq import *

class Solution:
    def smallestRange(self, nums):
        heap = []
        maxValue = float("-inf")

        for i in range(len(nums)):
            heappush(heap, (nums[i][0], i, 0))

            maxValue = max(maxValue, nums[i][0])

        result = []

        while heap:
            value, listIndex, elemIndex = heappop(heap)

            if not result or maxValue - value < result[1] - result[0]:
                result = [value, maxValue]

            if elemIndex + 1 < len(nums[listIndex]):
                heappush(heap, (nums[listIndex][elemIndex + 1], listIndex,
                                elemIndex + 1))
                maxValue = max(maxValue, nums[listIndex][elemIndex + 1])
            else:
                break
                
        return result
