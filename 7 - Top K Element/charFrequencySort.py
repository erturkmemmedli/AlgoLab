from heapq import heappush, heappop

class Solution:
    def frequencySort(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        heap = []
        for k, v in freq.items():
            heappush(heap, (-v, k))
        sortedString = ""
        for _ in range(len(heap)):
            count, char = heappop(heap)
            sortedString += char * (-count)
        return sortedString
        
# Official solution

from heapq import *
class Solution:
    def frequencySort(self, s):
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        maxHeap = []

        for char, frequency in freq.items():
            heappush(maxHeap, [-frequency, char])

        output = []

        while maxHeap:
            element = heappop(maxHeap)

            for i in range(-element[0]):
                output.append(element[1])

        return "".join(output)
