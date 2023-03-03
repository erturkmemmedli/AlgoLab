class Solution:
    def fib(self, n):
        self.memo = {}
        return self.dp(n)

    def dp(self, n):
        if n <= 1:
            return n
        
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n-1) + self.dp(n-2)
        return self.memo[n]
      
# Official solution

class Solution:
    def __init__(self):
        self.memo = [-1 for i in range(31)]
    
    def fib(self, n):
        if n < 2:
            return n

        if self.memo[n] >= 0:
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
