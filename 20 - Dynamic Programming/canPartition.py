class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 == 1:
            return False

        self.memo = {}
        return self.dp(nums, s//2, 0)

    def dp(self, nums, target, index):
        if target == 0:
            return True

        if target < 0 or index == len(nums):
            return False

        if (target, index) in self.memo:
            return self.memo[(target, index)]

        self.memo[(target, index)] = self.dp(nums, target - nums[index], index + 1) or self.dp(nums, target, index + 1)
        return self.memo[(target, index)]
        
# Official solution

class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        memo = [[-1 for i in range(target + 1)] for j in range(len(nums))]
        
        return self.helper(0, target, nums, memo)
    
    def helper(self, index, target, nums, memo):
        if target == 0:
            return True

        if index >= len(nums):
            return False

        if memo[index][target] != -1:
            return memo[index][target]
        
        include = False

        if target - nums[index] >= 0:
            include = self.helper(index + 1, target - nums[index], nums, memo)
            
        exclude = self.helper(index + 1, target, nums, memo)
        
        memo[index][target] = include or exclude
        
        return memo[index][target]
