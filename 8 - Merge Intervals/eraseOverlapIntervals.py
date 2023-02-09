class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: [x[0], x[1]])
        remove = 0
        last = intervals[0]
        for current in intervals[1:]:
            if current[1] < last[1]:
                remove += 1
                last = current
            elif current[0] < last[1]:
                remove += 1
            else:
                last = current
        return remove
        
# Official solution

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        n, count = len(intervals), 1

        if n == 0:
            return 0

        current = intervals[0]

        for i in range(n):
            if current[1] <= intervals[i][0]:
                count += 1
                current = intervals[i]

        return n - count
