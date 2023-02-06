class Solution:
    def findKthPositive(self, arr, k):
        last = 0
        length = len(arr)
        left, right = 0, length - 1
        missing = 0
        while left <= right:
            mid = left + (right - left) // 2
            count = mid - left + 1
            elements = arr[mid] - last - count
            if missing + elements < k:
                missing += elements
                last = arr[mid]
                left = mid + 1
            else:
                right = mid - 1
        return last + k - missing
        
# Official solution

class Solution:
    def findKthPositive(self, nums, k):
        i = 0
        
        while i < len(nums):
            j = nums[i] - 1
        
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        missingNumbers = []
        extraNumbers = set()
        
        for i in range(len(nums)):
            if len(missingNumbers) < k:
                if nums[i] != i + 1:
                    missingNumbers.append(i + 1)
                    extraNumbers.add(nums[i])
        
        i = 1
        n = len(nums)
        
        while len(missingNumbers) < k:
            candidateNumber = i + n
        
            if candidateNumber not in extraNumbers:
                missingNumbers.append(candidateNumber)
        
            i += 1

        return missingNumbers[k - 1]
