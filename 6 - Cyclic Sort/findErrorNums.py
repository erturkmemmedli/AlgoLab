class Solution:
    def findErrorNums(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num != i + 1:
                return [num, i + 1]
              
# Official solution

class Solution:
    def findErrorNums(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
