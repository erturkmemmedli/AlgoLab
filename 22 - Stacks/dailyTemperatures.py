class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        output = [None] * n
        stack = []
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
                
            output[i] = 0 if not stack else stack[-1][1] - i
            stack.append((temperatures[i], i))
            i -= 1
            
        return output
        
# Official solution

class Solution:
    def dailyTemperatures(self, temperatures):
        
        n = len(temperatures)
        j = n - 1
        stack = []
        output = [None] * n
        
        while j >= 0:
            number = temperatures[j]
            
            while stack and stack[-1][0] <= number:
                stack.pop()
            
            if not stack:
                output[j] = 0
            else:
                output[j] = stack[-1][1] - j
                
            stack.append([number, j])
            j -= 1
        
        
        return output
