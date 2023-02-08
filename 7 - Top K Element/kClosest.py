import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []
        for i in range(k):
            distance = self.squaredEuclideanDistance(points[i])
            heapq.heappush(heap, (-distance, points[i]))
        for i in range(k, len(points)):
            distance = self.squaredEuclideanDistance(points[i])
            if distance < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, points[i]))
        return [pts for _, pts in heap]
            
    def squaredEuclideanDistance(self, point):
        x, y = point
        return x ** 2 + y ** 2
        
# Official solution

from heapq import *
class Solution:
    def kClosest(self, points, k):
        maxHeap = []

        for i in range(0, len(points), 1):
            x = points[i][0]
            y = points[i][1]
            dist = (x * x) + (y * y)

            heappush(maxHeap, (-dist, [x, y]))

            if len(maxHeap) > k:
                heappop(maxHeap)

        output = []

        while len(maxHeap) > 0:
            output.append(heappop(maxHeap)[1])

        return output
