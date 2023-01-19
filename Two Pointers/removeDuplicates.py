class Solution:
    def removeDuplicates(self, nums):
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
            j += 1
        return i + 1
        
# Official solution

class Solution:
    def removeDuplicates(self, nums):
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left
