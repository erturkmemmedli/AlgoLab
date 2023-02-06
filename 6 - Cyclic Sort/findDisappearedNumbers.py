class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        missingElements = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missingElements.append(i + 1)
        return missingElements
      
# Official solution

class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        missingNumbers = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)

        return missingNumbers
