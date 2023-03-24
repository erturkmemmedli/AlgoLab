"""
Next Smaller Element
Given an array, return an output array containing the Next Smaller Element (NSE) for every element. 


The Next Smaller Element for an element x is the first smaller element on the right side of x in the array. For elements for which no smaller element exist, consider the next smaller element as -1. 


Example 1:

Input: [ 4 , 5 , 2 , 25 ]
Output:  [ 2, 2, -1, -1 ]
Example 2:

Input: [ 13 , 7, 6 , 12 ]
Output:  [ 7, 6 -1, -1 ]


Constraints:

1 <= arr.length <= 10^4
-10^9 <= arr[i] <= 10^9
"""

class Solution:
    def nextSmallerElement(self,arr):
        n = len(arr)
        stack = []
        output = [None] * n
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
                
            output[i] = stack[-1] if stack else -1
            
            stack.append(arr[i])
            i -= 1
            
        return output
        
# Official solution

class Solution:
    def nextSmallerElement(self,arr):
        
        n = len(arr) 
        stack = []
        output = [None] * n
        
        i = n - 1
        
        while i >= 0:
            number = arr[i]
            
            while stack and stack[-1] >= number:
                stack.pop()
            
            if not stack:
                output[i] = -1
            else:
                output[i] = stack[-1]
            
            stack.append(number)
            i -= 1
        
        return output
