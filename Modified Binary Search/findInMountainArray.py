
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target, mountain_arr):
        index = self.findPeakInMountainArray(mountain_arr)
        if mountain_arr.get(index) == target:
            return index
        idx = self.binarySearch(target, mountain_arr, 0, index - 1, False)
        return idx if idx != -1 else self.binarySearch(target, mountain_arr, index + 1, mountain_arr.length(), True)
        
    def findPeakInMountainArray(self, mountain_arr):
        length = mountain_arr.length()
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid + 1) > mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid
        return left
        
    def binarySearch(self, target, mountain_arr, left, right, reverse):
        while left <= right:
            mid = left + (right - left) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif (not reverse and val > target) or (reverse and val < target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
# Official solution

class Solution:
    def findInMountainArray(self, target: int, arr: "MountainArray") -> int:
        start = 1
        end = arr.length() - 2
        while True:
            middle = start + (end - start) // 2
            midLeftVal, midVal = arr.get(middle - 1), arr.get(middle)
            if midLeftVal < midVal > arr.get(middle + 1):
                i = middle
                break
            elif midLeftVal < midVal:
                start = middle + 1
            else:
                end = middle - 1

        start = 0
        end = i
        while start <= end:
            middle = start + (end - start) // 2
            midVal = arr.get(middle)
            if midVal == target:
                return middle
            elif midVal < target:
                start = middle + 1
            else:
                end = middle - 1

        start = i + 1
        end = arr.length() - 1
        while start <= end:
            middle = start + (end - start) // 2
            midVal = arr.get(middle)
            if midVal == target:
                return middle
            elif midVal < target:
                end = middle - 1
            else:
                start = middle + 1

        return -1
