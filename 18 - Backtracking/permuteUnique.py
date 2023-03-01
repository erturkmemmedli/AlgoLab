class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        self.result = []
        self.backtrack(nums, [])
        return self.result

    def backtrack(self, nums, path):
        if not nums:
            self.result.append(path)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])
            
# Official solution

class Solution:
    def permuteUnique(self, nums):
        result = []

        nums.sort()

        visited = [False] * len(nums)
        self.backtracking(result, nums, [], visited)

        return result 
        
    def backtracking(self, result, nums, path, visited):
        if len(nums) == len(path):
            result.append(path[:])
        
        for i in range(len(nums)):
            if visited[i] or i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True

            path.append(nums[i])
            self.backtracking(result, nums, path, visited)
            visited[i] = False

            path.pop()
