class Solution:
    def findMaxAverage(self, nums, k):
        maxAverage = -float("inf")
        windowSum = sum(nums[:k])
        maxAverage = max(maxAverage, windowSum / k)
        for i in range(len(nums) - k):
            windowSum += nums[i + k] - nums[i]
            maxAverage = max(maxAverage, windowSum / k)
        return maxAverage
      
# Official solution given

class Solution:
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[:k])
        maxAverage = windowSum / k

        for i in range(len(nums) - k):
            windowSum = windowSum - nums[i] + nums[i + k]
            average = windowSum / k
            maxAverage = max(maxAverage, average)

        return maxAverage
