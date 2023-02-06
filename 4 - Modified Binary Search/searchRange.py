class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        result[0] = self.binarySearch(nums, target, True)
        result[1] = self.binarySearch(nums, target, False)
        return result
        
    def binarySearch(self, nums, target, findFirstIndex):
        targetIndex = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                targetIndex = mid
                if findFirstIndex:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return targetIndex
        
# Official solution

class Solution:
    def searchRange(self, arr, target):
        result = [-1, -1]
        result[0] = self.binarySearch(arr, target, True)
        result[1] = self.binarySearch(arr, target, False)
        return result

    def binarySearch(self, arr, target, findFirstIndex):
        targetIndex = -1
        start, end = 0, len(arr) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if arr[middle] == target:
                targetIndex = middle
                if findFirstIndex:
                    end = middle - 1
                else:
                    start = middle + 1
            elif target < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return targetIndex
