class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        self.memo = {}
        return self.dp(obstacleGrid, 0, 0)

    def dp(self, grid, row, col):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1
        
        if row == len(grid) or col == len(grid[0]) or grid[row][col] == 1:
            return 0

        if (row, col) in self.memo:
            return self.memo[(row, col)]

        self.memo[(row, col)] = self.dp(grid, row + 1, col) + self.dp(grid, row, col + 1)
        return self.memo[(row, col)]
        
# Official solution

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        return self.helper(obstacleGrid, 0, 0, ROWS, COLS, memo)
        
    def helper(self, grid, row, col, ROWS, COLS, memo):
        if row == ROWS or col == COLS or grid[row][col] == 1:
            return 0
        
        if row == ROWS - 1 and col == COLS - 1:
            if grid[row][col] == 1:
                return 0
        
            return 1
        
        if memo[row][col] > 0:
            return memo[row][col]

        memo[row][col] = self.helper(grid, row+1, col, ROWS, COLS, memo) + \
                       self.helper(grid, row, col+1, ROWS, COLS, memo)
                       
        return memo[row][col]
