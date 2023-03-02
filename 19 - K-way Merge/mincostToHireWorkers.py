from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        data = sorted([(wage[i]/quality[i], quality[i], wage[i]) for i in range(len(wage))])
        heap = []
        min_wage = float("inf")
        sum_heap = 0

        for factor, q, w in data:
            heappush(heap, -q)
            sum_heap += q

            if len(heap) > K:
                sum_heap += heappop(heap)

            if len(heap) == K:
                min_wage = min(min_wage, factor * sum_heap)
            
        return min_wage
      
# Official solution

from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = [(wage[i] / quality[i], quality[i]) for i in range(len(quality))]

        workers.sort()
        
        heap = []
        res = float('inf')
        qualitySum = 0
        
        for ratio, quality in workers:
            heappush(heap, -quality)
            qualitySum += quality
            
            if len(heap) > K:
                qualitySum += heappop(heap)
            
            if len(heap) == K:
                res = min(res, qualitySum * ratio)
                
        return res
