class Solution:
    def combinationSum(self, candidates, target):
        self.result =[]
        self.backtrack(candidates, target, [], 0)
        return list(self.result)

    def backtrack(self, nums, target, currState, currSum):
        if currSum > target:
            return
        elif currSum == target:
            self.result.append(currState[:])
            return
        for i in range(len(nums)):
            currState.append(nums[i])
            currSum += nums[i]
            self.backtrack(nums[i:], target, currState, currSum)
            currSum -= nums[i]
            currState.pop()
            
# Official solution

class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        self.backtrack(candidates, target, [], 0, result)

        return result
    
    def backtrack(self, candidates, remaining, combination, start, result):
        if remaining == 0:
            result.append(list(combination))

            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])

            self.backtrack(candidates, remaining - candidates[i], combination, i, result)

            combination.pop()
