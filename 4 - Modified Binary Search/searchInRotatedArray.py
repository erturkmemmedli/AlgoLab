class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] >= nums[left] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] <= nums[right] or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        
# Official solution

class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2

            if nums[middle] == target:
                return middle

            if nums[start] <= nums[middle]:
                if target < nums[start] or target > nums[middle]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if target > nums[end] or target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1

        return -1
