class Solution:
    def fib(self, n):
        if n < 2: return n
        prev, curr = 0, 1
        for _ in range(n-1):
            prev, curr = curr, prev + curr
        return curr
		
# Official solution given

class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        lastValue, scndLastValue = 0, 1
        for i in range(2, n + 1):
            temp = scndLastValue + lastValue
            lastValue = scndLastValue
            scndLastValue = temp
        return scndLastValue
