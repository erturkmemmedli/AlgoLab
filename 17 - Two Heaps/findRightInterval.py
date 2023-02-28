from heapq import heappush, heappop

class Solution:
    def findRightInterval(self, intervals):
        right_intervals = [-1 for i in range(len(intervals))]
        start_heap = []
        end_heap = []

        for i, [start, end] in enumerate(intervals):
            heappush(start_heap, (start, i))
            heappush(end_heap, (end, i))

        while start_heap and end_heap:
            if start_heap[0][0] < end_heap[0][0]:
                heappop(start_heap)
            else:
                _, index = heappop(end_heap)
                right_intervals[index] = start_heap[0][1]

        return right_intervals
        
# Official solution

from heapq import *

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)

        if n == 0:
            return []

        output = [-1] * len(intervals)

        if n == 1:
            return output
        
        startHeap = []
        endHeap = []

        for i in range(len(intervals)):
            heappush(startHeap, (intervals[i][0], i))
            heappush(endHeap, (intervals[i][1], i))
        
        while endHeap:
            parsing = heappop(endHeap)

            while startHeap:
                if startHeap[0][0] >= parsing[0]:
                    output[parsing[1]] = startHeap[0][1]

                    break
                else:
                    heappop(startHeap)
                    
        return output
