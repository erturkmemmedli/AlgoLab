class Solution:
    def findDuplicate(self, nums):
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
        
# Official solution

class Solution:
    def findDuplicate(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != i + 1:
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1

        return -1
