class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        stack = []
        next_greater = {}
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                
            next_greater[nums2[i]] = stack[-1] if stack else -1
            
            stack.append(nums2[i])
            i -= 1
            
        return [next_greater[i] for i in nums1]
        
# Official solution

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        # Create a dictionary to store the indices of nums1 for quick lookup
        nums1IndexDict = {}
        for i in range(len(nums1)):
            nums1IndexDict[nums1[i]] = i
        
       
        # Initialize the stack and the output list
        stack = []
        output = [-1]*len(nums1)
        
        j = len(nums2) - 1
        while j >= 0:
            number = nums2[j]
            if number in nums1IndexDict:
                while stack and stack[-1] <= number:
                    stack.pop()
                    
                if stack:
                    output[nums1IndexDict[number]] = stack[-1]
            j -= 1
            stack.append(number)
        
        return output
