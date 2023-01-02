class Solution:
    def getConcatenation(self, nums):
        return nums + nums
		
# Official solution given

class Solution:
    def getConcatenation(self, nums):
        ans = []
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])
        return ans
