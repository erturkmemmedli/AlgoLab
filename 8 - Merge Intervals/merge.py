class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        for current in intervals[1:]:
            last = result[-1]
            if last[1] >= current[0]: 
                start = last[0]
                end = max(current[1], last[1])
                result[-1] = [start, end]
            else:
                result.append(current)
        return result
      
# Official solution

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for interval in intervals[1:]:
            intervalA = result[-1]
            intervalB = interval

            if intervalA[1] >= intervalB[0]:
                result[-1] = [intervalA[0], max(intervalA[1], intervalB[1])]
            else:
                result.append(intervalB)

        return result
