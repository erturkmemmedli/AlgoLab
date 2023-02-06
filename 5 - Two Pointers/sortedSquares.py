class Solution:
    def sortedSquares(self, nums):
        positiveFirst = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                positiveFirst = i
                break
        negativeLast = positiveFirst - 1
        result = []
        while negativeLast >= 0 and positiveFirst < len(nums):
            if -nums[negativeLast] <= nums[positiveFirst]:
                result.append(nums[negativeLast] ** 2)
                negativeLast -= 1
            else:
                result.append(nums[positiveFirst] ** 2)
                positiveFirst += 1
        while negativeLast >= 0:
            result.append(nums[negativeLast] ** 2)
            negativeLast -= 1
        while positiveFirst < len(nums):
            result.append(nums[positiveFirst] ** 2)
            positiveFirst += 1
        return result
        
# Official solution

class Solution:
    def sortedSquares(self, nums):
        squares = [None] * len(nums)
        left = 0
        right = len(nums) - 1
        highestSquareIndex = len(nums) - 1
        while left <= right:
            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare > rightSquare:
                squares[highestSquareIndex] = leftSquare
                left += 1
            else:
                squares[highestSquareIndex] = rightSquare
                right -= 1
            highestSquareIndex -= 1

        return squares
