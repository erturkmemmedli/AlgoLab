class Solution:
    def missingNumber(self, nums):
        nums.append(-1)
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] != nums[j] and nums[i] != -1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num == -1:
                return i
                
# Official solution

class Solution:
    def missingNumber(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i]

            if nums[i] < len(nums) and nums[i] != i:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
