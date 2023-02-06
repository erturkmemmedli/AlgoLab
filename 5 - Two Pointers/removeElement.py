class Solution:
    def removeElement(self, nums, val):
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i
        
# Official solution

class Solution:
    def removeElement(self, nums, val):
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
