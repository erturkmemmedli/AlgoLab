class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.result = []
        self.backtrack(candidates, target, [])
        return self.result

    def backtrack(self, nums, target, path):
        if target < 0:
            return
        elif target == 0:
            self.result.append(path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrack(nums[i+1:], target - nums[i], path)
            path.pop()
            
# Official solution

class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []

        self.backtrack(result, nums, [], target, 0)

        return result
    
    def backtrack(self, result, nums, path, remaining, start):
        if remaining < 0:
            return

        if remaining == 0:
            result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: 
                continue

            path.append(nums[i])

            self.backtrack(result, nums, path, remaining - nums[i], i+1)

            path.pop()
