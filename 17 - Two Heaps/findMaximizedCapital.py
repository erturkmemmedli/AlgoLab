from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        usableHeap = []
        reserveHeap = []

        for i in range(len(profits)):
            if capital[i] <= w:
                heappush(usableHeap, (-profits[i], capital[i]))
            else:
                heappush(reserveHeap, (capital[i], profits[i]))
    
        while k:
            if not usableHeap:
                break
                
            profit, capital = heappop(usableHeap)
            w -= profit
            k -= 1

            while reserveHeap and reserveHeap[0][0] <= w:
                capital, profit = heappop(reserveHeap)
                heappush(usableHeap, (-profit, capital))

        return w
        
# Official solution

from heapq import *

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        currentCapital = w
        capitalsMinHeap = []
        profitsMaxHeap = []

        for x in range(0, len(capital)):
            heappush(capitalsMinHeap, (capital[x], x))

        for _ in range(k):

            while capitalsMinHeap and capitalsMinHeap[0][0] <= currentCapital:
                c, i = heappop(capitalsMinHeap)
                heappush(profitsMaxHeap, (-profits[i], i))
            
            if not profitsMaxHeap:
                break

            j = -heappop(profitsMaxHeap)[0]
            currentCapital = currentCapital + j

        return currentCapital
