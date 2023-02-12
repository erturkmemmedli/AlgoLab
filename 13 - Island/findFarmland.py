class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        farmlandCoordinates = []
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    r1, c1 = i, j
                    r2, c2 = self.dfs(land, m, n, i, j, r1, c1)
                    farmlandCoordinates.append([r1, c1, r2, c2])
        return farmlandCoordinates

    def dfs(self, land, m, n, row, col, pRow, pCol):
        if m > row >= 0 <= col < n and land[row][col]:
            land[row][col] = 0
            up = self.dfs(land, m, n, row - 1, col, row, col)
            down = self.dfs(land, m, n, row + 1, col, row, col)
            left = self.dfs(land, m, n, row, col - 1, row, col)
            right = self.dfs(land, m, n, row, col + 1, row, col)
            pRow = max(pRow, up[0], down[0], left[0], right[0])
            pCol = max(pCol, up[1], down[1], left[1], right[1])
        return pRow, pCol
        
# Official solution

class Solution:
    def findFarmland(self, grid):
        self.answer = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    (x, y) = self.helper(i, j, grid)
                    
                    self.answer.append([i, j, x, y])

        return self.answer

    def helper(self, i, j, grid):
        if i < 0 or j < 0 or j >= len(grid[0]) or 
           i >= len(grid) or grid[i][j] == 0:
            return (0, 0)

        (nx, ny) = (i, j)
        grid[i][j] = 0
        directions = [(1, 0), (0, 1)]
        
        for x, y in directions:
            (nx, ny) = max((nx, ny), self.helper(i + x, j + y, grid))
        
        return (nx, ny)
