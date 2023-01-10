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
