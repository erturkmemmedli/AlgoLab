class Solution:
    def uniquePaths(self, m, n):
        self.memo = {}
        return self.dp(m, n, 0, 0)

    def dp(self, m, n, row, col):
        if row == m-1 and col == n-1:
            return 1

        if row == m or col == n:
            return 0

        if (row, col) in self.memo:
            return self.memo[(row, col)]

        self.memo[(row, col)] = self.dp(m, n, row + 1, col) + self.dp(m, n, row, col + 1)
        return self.memo[(row, col)]
        
# Official solution

class Solution:
    def uniquePaths(self, m, n):
        memo = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                memo[col][row] = memo[col - 1][row] + memo[col][row - 1]

        return memo[m - 1][n - 1]
