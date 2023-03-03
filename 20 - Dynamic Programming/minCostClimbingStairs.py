class Solution:
    def minCostClimbingStairs(self, cost):
        self.memo = {}
        self.dp(cost, 0)
        return min(self.memo[0], self.memo[1])

    def dp(self, cost, index):
        if index >= len(cost):
            return 0

        if index in self.memo:
            return self.memo[index]

        self.memo[index] = cost[index] + min(self.dp(cost, index + 1), self.dp(cost, index + 2))
        return self.memo[index]
        
# Official solution

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = [-1 for _ in range(n + 1)]

        return min(self.helper(cost, n-1, memo), self.helper(cost, n-2, memo))
    
    def helper(self, cost, n, memo):
        if n < 0:
            return 0

        if n == 0:
            return cost[0]
            
        if memo[n] != -1:
            return memo[n]
            
        memo[n] = min(self.helper(cost, n-1, memo), \
                  self.helper(cost, n-2, memo)) + cost[n]
                  
        return memo[n]
