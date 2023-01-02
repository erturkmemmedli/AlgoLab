class Solution:
    def buildArray(self, nums):
        array = []
        for num in nums:
            array.append(nums[num])
        return array
		
# Official solution given

class Solution:
    def buildArray(self, nums):
        answer = []
        for i in range(len(nums)):
            answer.append(nums[nums[i]])
        return answer

