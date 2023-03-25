class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = int(matrix[i][j]) * heights[j] + int(matrix[i][j])
            
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            max_area = max(max_area, heights[i])
            width = 1

            while stack and stack[-1][0] >= heights[i]:
                h, w = stack.pop()
                
                if stack and stack[-1][0] >= heights[i]:
                    stack[-1] = [min(stack[-1][0], h), stack[-1][1] + w]
                    max_area = max(max_area, stack[-1][0] * stack[-1][1])
                    
                else:
                    width += w
                    max_area = max(max_area, min(h, heights[i]) * width)
                    break
        
            stack.append([heights[i], width])
            i += 1

        while len(stack) > 1:
            h, w = stack.pop()
            stack[-1] = [stack[-1][0], stack[-1][1] + w]
            max_area = max(max_area, stack[-1][0] * stack[-1][1])
            
        return max_area
        
# Official solution

class Solution:
    def maximalRectangle(self, matrix):
        heights = [0] * len(matrix[0])
        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
                    
            area = self.largestRectangleArea(heights)
            maxArea = max(area, maxArea)
        
        return maxArea

    def largestRectangleArea(self, heights):
        
        nextSmallest = self.findNextSmallest(heights)
        previousSmallest = self.findPreviousSmallest(heights)
        maxArea = 0
        
        for i in range(len(heights)):
            width = nextSmallest[i] - previousSmallest[i] - 1
            height = heights[i]
            
            area = width * height
            maxArea = max(area, maxArea)
        
        return maxArea
    
    def findNextSmallest(self, arr):
        
        stack = []
        output = [None] * len(arr)
        i = len(arr) - 1
        
        while i >= 0:
            number = arr[i]
            
            while stack and stack[-1][0] >= number:
                stack.pop()
            
            if not stack:
                output[i] = len(arr)
            else:
                output[i] = stack[-1][1]
            
            stack.append([number, i])
            i -= 1
        
        return output
                
    def findPreviousSmallest(self, arr):
        
        stack = []
        output = [None] * len(arr)
        i = 0
        
        while i < len(arr):
            number = arr[i]
            
            while stack and stack[-1][0] >= number:
                stack.pop()
            
            if not stack:
                output[i] = -1
            else:
                output[i] = stack[-1][1]
            
            stack.append([number, i])
            i += 1
        
        return output
