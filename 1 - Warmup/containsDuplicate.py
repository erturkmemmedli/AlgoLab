class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
		
# Official solution given

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
