class Solution:
    def climbStairs(self, n):
        self.memo = {}
        return self.dp(n)

    def dp(self, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 0

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n-1) + self.dp(n-2)
        return self.memo[n]
        
# Official solution

class Solution:
    def __init__(self):
        self.memo = [0 for _ in range(46)]

    def climbStairs(self, n):
        if n <= 2:
            return n
        elif self.memo[n] != 0:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.memo[n]
