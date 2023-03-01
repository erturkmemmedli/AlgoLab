class Solution:
    def subsets(self, nums):
        result = []
        self.backtrack(result, nums, [], 0)
        return result

    def backtrack(self, result, nums, currState, start):
        result.append(currState[:])
        for i in range(start, len(nums)):
            currState.append(nums[i])
            self.backtrack(result, nums, currState, i + 1)
            currState.pop()
            
# Official solution

class Solution:
    def subsets(self, nums):
        result = []
        self.backtrack(nums, [], result, 0)

        return result
    
    def backtrack(self, nums, path, result, start):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])

            self.backtrack(nums, path, result, i + 1)

            path.pop()
