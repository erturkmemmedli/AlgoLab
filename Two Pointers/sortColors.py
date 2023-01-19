class Solution:
    def sortColors(self, nums):
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        j = i
        while j < len(nums):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
        
# Official solution

class Solution:
    def sortColors(self, nums):
        p0 = 0
        p2 = len(nums) - 1
        p1 = 0

        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
                
        return nums
