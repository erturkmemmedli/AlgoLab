class Solution:
    def singleNumber(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result
		
# Official solution given

class Solution:
    def singleNumber(self, nums):
        array = []

        for number in nums:
            if number not in array:
                array.append(number)
            else:
                array.remove(number)

        return array[0]