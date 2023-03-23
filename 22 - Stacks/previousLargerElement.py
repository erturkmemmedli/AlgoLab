"""
Previous Greater Element
Given an array, return an output array containing the Previous Greater Element (PGE) for every element. 

The Previous Greater Element for an element x is the first greater element on the left side of x in the array. For elements for which no greater element exist, consider the previous greater element as -1. 

Example 1:
Input: [ 4 , 5 , 2 , 25 ]
Output:  [ -1, -1, 5, -1 ]

Explanation: except 2 no element has an element greater than them present on the left side

Example 2:
Input: [ 13 , 7, 6 , 12 ]
Output:  [ -1, 13, 7, 13 ]

Constraints:
1 <= arr.length <= 10^4
-10^9 <= arr[i] <= 10^9
"""

class Solution:
    def previousLargerElement(self,arr):
        n = len(arr)
        stack = []
        output = [None] * n
        i = 0
        
        while i < n:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            output[i] = stack[-1] if stack else -1
            
            stack.append(arr[i])
            i += 1
            
        return output
        
# Official solution

class Solution:
    def previousLargerElement(self,arr):
        
        n = len(arr) 
        stack = []
        output = [None] * n
        
        i = 0
        
        while i < n:
            number = arr[i]
            
            while stack and stack[-1] <= number:
                stack.pop()
            
            if not stack:
                output[i] = -1
            else:
                output[i] = stack[-1]
            
            stack.append(number)
            i += 1
        
        return output
