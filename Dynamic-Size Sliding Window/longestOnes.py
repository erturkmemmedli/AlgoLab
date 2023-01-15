class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeroCount = 0
        maxLength = 0
        for right, num in enumerate(nums):
            if num == 1:
                maxLength = max(maxLength, right - left + 1)
            else:
                zeroCount += 1
                while zeroCount > k:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
        maxLength = max(maxLength, right - left + 1)    
        return maxLength

# Official solution

class Solution:
    def longestOnes(self, nums, k):
        if k == len(nums):
            return k

        windowStart = 0
        longest = 0
        zeros = 0

        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 0:
                zeros += 1

            while zeros > k:
                if nums[windowStart] == 0:
                    zeros -= 1
                windowStart += 1

            longest = max(longest, windowEnd - windowStart + 1)

        return longest
