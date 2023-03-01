class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        self.result = []
        self.backtrack(nums, [], 0)
        return self.result

    def backtrack(self, nums, currState, start):
        if currState not in self.result:
            self.result.append(currState)
        for i in range(start, len(nums)):
            self.backtrack(nums, currState + [nums[i]], i + 1)
            
# Alternative solution

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.backtrack(nums, [], 0)
        return self.result

    def backtrack(self, nums, currState, start):
        self.result.append(currState)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums, currState + [nums[i]], i + 1)
            
# Official solution

class Solution:
    def subsetsWithDup(self, nums):
        result = []

        nums.sort()

        self.backtrack(nums, [], result, 0)

        return result
    
    def backtrack(self, nums, path, result, start):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])

            self.backtrack(nums, path, result, i + 1)

            path.pop()
