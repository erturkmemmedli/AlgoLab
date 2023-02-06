class Solution:
    def findDuplicates(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        duplicates = []
        for i, num in enumerate(nums):
            if num != i + 1:
                duplicates.append(num)
        return duplicates
        
# Official solution

class Solution:
    def findDuplicates(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        duplicateNumbers = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicateNumbers.append(nums[i])

        return duplicateNumbers
