class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = -1
        maxOnes = 0
        for right, num in enumerate(nums):
            if num == 1:
                maxOnes = max(maxOnes, right - left)
            else:
                left = right
        return maxOnes

# Official solution

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxLength = 0
        windowStart = 0

        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 0:
                windowStart = windowEnd + 1
            else:
                currentLength = windowEnd - windowStart + 1
                maxLength = max(maxLength, currentLength)
        return maxLength
