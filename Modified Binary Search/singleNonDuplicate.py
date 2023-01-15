class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if len(nums) % 4 == 1:
                if nums[mid] == nums[mid - 1]:
                    right = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    left = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
                else:
                    return nums[mid]
        return nums[left]
        
# Official official

class Solution:
    def singleNonDuplicate(self, nums):
        start = 0
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start) // 2
            areEven = (end - middle) % 2 == 0

            if nums[middle + 1] == nums[middle]:
                if areEven:
                    start = middle + 2
                else:
                    end = middle - 1

            elif nums[middle - 1] == nums[middle]:
                if areEven:
                    end = middle - 2
                else:
                    start = middle + 1

            else:
                return nums[middle]

        return nums[start]
