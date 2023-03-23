"""
Next Greater Element
Given an array, return an output array containing the Next Greater Element (NGE) for every element. 

The Next Greater Element for an element x is the first greater element on the right side of x in the array. For elements for which no greater element exist, consider the next greater element as -1. 

Example 1:
Input: [ 4 , 5 , 2 , 25 ]
Output: [ 5, 25, 25, -1 ]

Explanation: except 25 every element has an element greater than them present on the right side

Example 2:
Input: [ 13 , 7, 6 , 12 ]
Output:  [ -1, 12, 12, -1 ]

Constraints:
1 <= arr.length <= 10^4
-10^9 <= arr[i] <= 10^9
"""

class Solution:
    def nextLargerElement(self,arr):
        n = len(arr)
        stack = []
        output = [None] * n
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            if stack:
                output[i] = stack[-1]
            else:
                output[i] = -1
                
            stack.append(arr[i])
            i -= 1
        
        return output
        
# Official solution

class Solution:
    def nextLargerElement(self,arr):
        
        n = len(arr) 
        stack = []
        output = [None] * n
        
        i = n - 1
        
        while i >= 0:
            number = arr[i]
            
            while stack and stack[-1] <= number:
                stack.pop()
            
            if not stack:
                output[i] = -1
            else:
                output[i] = stack[-1]
            
            stack.append(number)
            i -= 1
        
        return output
