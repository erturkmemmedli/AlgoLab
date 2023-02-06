class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
                
# Official solution

class Solution:
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1
        currentSum = 0

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum == target:
                return [left + 1, right + 1]
            elif currentSum < target:
                left += 1
            else:
                right -= 1

        return []
