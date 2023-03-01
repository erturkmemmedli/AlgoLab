from heapq import *

class Solution:  
    def kthSmallest(self, matrix, k):
        heap = []

        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], i, 0))

        while k:
            root, row, col = heappop(heap)
            k -= 1
            
            if col + 1 < len(matrix[0]):
                heappush(heap, (matrix[row][col + 1], row, col + 1))
        
        return root
      
# Official solution

from heapq import *

class Solution:  
    def kthSmallest(self, matrix, k):
        ROWS, COLS = len(matrix), len(matrix[0]) 
        minHeap = []  

        for row in range(min(k, ROWS)):
            heappush(minHeap, (matrix[row][0], row, 0))

        output = -1 

        for i in range(k):
            output, row, col = heappop(minHeap)

            if col + 1 < COLS: 
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))

        return output
