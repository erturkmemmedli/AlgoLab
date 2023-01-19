class Solution:
    def maxArea(self, height):
        left, right, maxArea = 0, len(height) - 1, 0
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        
# Official solution

class Solution:
    def maxArea(self, height):

        maxValue = 0
        left = 0
        right = len(height) - 1

        while left < right:
            currArea = min(height[left], height[right]) * (right - left)
            maxValue = max(maxValue, currArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxValue
