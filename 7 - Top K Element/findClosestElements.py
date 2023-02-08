import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))
        for i in range(k, len(arr)):
            if abs(arr[i] - x) < -heap[0][0] or (abs(arr[i] - x) == -heap[0][0] and arr[i] < heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))
        return sorted([element for distance, element in heap])
        
# Official solution

from heapq import *
class Solution:
    def findClosestElements(self, arr, k, x):
        index = self.binarySearch(arr, x)

        low, high = index - k, index + k
        low = max(low, 0) 
        high = min(high, len(arr) - 1)
        minHeap = []
       
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))

        output = []

        for _ in range(k):
            output.append(heappop(minHeap)[1])

        output.sort()

        return output

    def binarySearch(self, arr,  target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low > 0:
            return low - 1

        return low
