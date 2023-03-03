class Solution:
    def findTargetSumWays(self, nums, target):
        self.memo = {}
        return self.dp(nums, target, 0)

    def dp(self, nums, target, index):
        if index == len(nums):
            return 1 if target == 0 else 0
        
        if (target, index) in self.memo:
            return self.memo[(target, index)]

        self.memo[(target, index)] = self.dp(nums, target - nums[index], index + 1) + self.dp(nums, target + nums[index], index + 1)
        return self.memo[(target, index)]
        
# Official solution

class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}
        return self.helper(0, nums, target, memo)
    
    def helper(self, index, nums, target, memo):
        if target == 0 and index >= len(nums):
            return 1

        if index >= len(nums):
            return 0

        key = str(index) + "," + str(target)
        
        if key in memo:
            return memo[key]
        
        decisionA = self.helper(index + 1, nums, target - nums[index], memo)
        decisionB = self.helper(index + 1, nums, target + nums[index], memo)
        
        memo[key] = decisionA + decisionB
        
        return memo[key]
