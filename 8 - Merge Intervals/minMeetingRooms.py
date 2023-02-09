'''
Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 10⁴
0 <= starti < endi <= 10⁶
'''

class Solution:
    def minMeetingRooms(self, intervals):
        points = []
        for start, end in intervals:
            points.append((start, 0))
            points.append((end, 1))
        points.sort(key = lambda x: x[0])
        roomRequired = 0
        currentRoom = 0
        for point, isEnd in points:
            if not isEnd:
                currentRoom += 1
            else:
                currentRoom -= 1
            roomRequired = max(roomRequired, currentRoom)
        return roomRequired
      
# Official solution

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        rooms = []

        for interval in intervals:
            start, end = interval
            heappush(rooms, end)

            if rooms[0] <= start:
                heappop(rooms)

        return len(rooms)
