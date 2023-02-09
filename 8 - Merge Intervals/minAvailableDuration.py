'''
Meeting Scheduler
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other.
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Constraints:

1 <= slots1.length, slots2.length <= 10⁴
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10⁹
1 <= duration <= 10⁶
'''

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        interval, i, j = [], 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] <= slots2[j][0]:
                i += 1
            elif slots2[j][1] <= slots1[i][0]:
                j += 1
            else:
                start = max(slots1[i][0], slots2[j][0])
                end = min(slots1[i][1], slots2[j][1])
                if end - start >= duration:
                    interval = [start, start + duration]
                    break
                else:
                    if slots1[i][1] < slots2[j][1]:
                        i += 1
                    else:
                        j += 1
        return interval
      
# Official solution

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()
        firstPointer, secondPointer = 0, 0

        while firstPointer < len(slots1) and secondPointer < len(slots2):
            firstSlotMeeting, secondSlotMeeting = (
                slots1[firstPointer],
                slots2[secondPointer],
            )

            start = max(firstSlotMeeting[0], secondSlotMeeting[0])
            end = min(firstSlotMeeting[1], secondSlotMeeting[1])

            if start + duration <= end:
                return [start, start + duration]
            elif firstSlotMeeting[1] < secondSlotMeeting[1]:
                firstPointer += 1
            else:
                secondPointer += 1

        return []
