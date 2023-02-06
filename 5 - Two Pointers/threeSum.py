class Solution:
    def threeSum(self, nums):
        self.triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if not self.triplets or nums[i] != self.triplets[-1][0]:
                self.twoSum(nums, i + 1, -nums[i])
        return self.triplets
        
    def twoSum(self, nums, index, target):
        i, j = index, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                small, big = nums[i], nums[j]
                self.triplets.append([-target, small, big])
                i += 1
                while nums[i] == small and i < j:
                    i += 1
                j -= 1
                while nums[i] == big and i < j:
                    j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
                
# Official solution

class Solution(object):
    def threeSum(self, arr):
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            self.searchPair(arr, -arr[i], i + 1, triplets)

        return triplets

    def searchPair(self, arr, targetSum, left, triplets):
        right = len(arr) - 1
        while left < right:
            currentSum = arr[left] + arr[right]
            if currentSum == targetSum:
                triplets.append([-targetSum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif targetSum > currentSum:
                left += 1
            else:
                right -= 1
