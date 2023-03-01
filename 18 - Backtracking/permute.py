class Solution:
    def permute(self, nums):
        self.result = []
        self.backtrack(nums, [], len(nums))
        return self.result

    def backtrack(self, nums, path, length):
        if len(path) == length:
            self.result.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:], path, length)
            path.pop()
            
# Official solution

class Solution:
    def permute(self, nums):
        result = []
        self.backtrack(nums, [], result)

        return result


    def backtrack(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:])

        for i in range(len(nums)):
            if nums[i] in path:
                continue

            path.append(nums[i])

            self.backtrack(nums, path, result)

            path.pop()
