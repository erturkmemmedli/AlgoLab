class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            else:
                break
        if result and newInterval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            result.append(newInterval)
        for current in intervals[i:]:
            last = result[-1]
            if current[0] > last[1]:
                result.append(current)
            else:
                start = last[0]
                end = max(last[1], current[1])
                result[-1] = [start, end]
        return result    
        
# Official solution

class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        result = []

        for current in intervals:
            if newInterval[0] <= current[1]:
                break
            else:
                result.append(current)
                i += 1

        result.append(newInterval)

        for i in range(i, len(intervals)):
            previous = result[-1]
            current = intervals[i]

            if current[0] <= previous[1]:
                start = min(previous[0], current[0])
                end = max(current[1], previous[1])
                result[-1] = [start, end]
            else:
                result.append(intervals[i])

        return result
