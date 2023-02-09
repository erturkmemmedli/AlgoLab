'''
Employee Free Time
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined). 
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 
Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10⁸
'''

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule):
        allIntervals = []
        for intervals in schedule:
            for interval in intervals:
                allIntervals.append(interval)
        allIntervals.sort(key = lambda x: x.start)
        mergedIntervals = [allIntervals[0]]
        start, end = allIntervals[0].start, allIntervals[0].end
        for interval in allIntervals[1:]:
            last = mergedIntervals[-1]
            if interval.start <= last.end:
                start = last.start
                end = max(last.end, interval.end)
                newInterval = Interval(start, end)
                mergedIntervals[-1] = newInterval
            else:
                mergedIntervals.append(interval)
        freeIntervals = []
        for i in range(1, len(mergedIntervals)):
            start = mergedIntervals[i-1].end
            end = mergedIntervals[i].start
            freeTime = Interval(start, end)
            freeIntervals.append(freeTime)
        return freeIntervals
      
# Official solution

class Solution:
     def employeeFreeTime(self, schedules):

        if not schedules or not schedules[0]:
            return []

        merged = []

        for schedule in schedules:
            merged += schedule

        merged.sort(key=lambda x: x.start)

        freeTime = []
        prev = merged[0]
        start, end = prev.start, prev.end

        for i in range(1, len(merged)):
            current = merged[i]

            if end >= current.start:
                start = min(start, current.start)
                end = max(end, current.end)
            else:
                freeTime.append(Interval(end, current.start))
                start, end = current.start, current.end

        return freeTime
