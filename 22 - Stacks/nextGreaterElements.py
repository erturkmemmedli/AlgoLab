class Solution:
    def nextGreaterElements(self, nums):
        idx = nums.index(max(nums))
        nums = nums[idx+1:] + nums[:idx+1]
        
        n = len(nums)
        stack = []
        output = [None] * n
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
                
            output[i] = stack[-1] if stack else -1
            stack.append(nums[i])
            i -= 1
            
        return output[n-idx-1:] + output[:n-idx-1]
        
# Official solution

class Solution:
    def nextGreaterElements(self, nums):
        
        # Initialize the stack and the output list
        stack = []
        output = [None] * len(nums)
        
        n = len(nums)
        # Start from the last element in the circular array
        i = 2* (n - 1)

        while i >= 0:
            # Calculate the index of the current element in the circular array
            j = i % n
            number = nums[j]
            while stack and stack[-1] <= number:
                stack.pop()
            
            if not stack:
                output[j] = -1
            else:
                output[j] = stack[-1]
            
            stack.append(number)
            i -= 1
        
        return output
