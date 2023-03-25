class Solution:
    def removeKdigits(self, num, k):
        stack = []

        i = 0
        while i < len(num):
            while stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
                if k == 0:
                    break 
            stack.append(num[i])
            i += 1
            if k == 0:
                break

        while k:
            stack.pop()
            k -= 1

        j = 0     
        while j < len(stack):
            if stack[j] == '0':
                j += 1
            else:
                break

        result = "".join(stack[j:])
        
        if result:
            result += num[i:]
            return result

        while i < len(num):
            if num[i] == '0':
                i += 1
            else:
                break
            
        result = num[i:]
        return result if result else "0"
        
# Official solution

class Solution:
    def removeKdigits(self, num, k):
        
        stack = []
        
        for number in num:
            
            while k != 0 and stack and stack[-1] > number:
                stack.pop()
                k -= 1
            
            stack.append(number)
        
       
        if k != 0:
            stack = stack[:-k]
        
        return "".join(stack).lstrip('0') or "0"
