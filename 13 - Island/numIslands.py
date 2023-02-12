class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        numOfIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    self.traverseIsland(grid, m, n, i, j)
        return numOfIslands

    def traverseIsland(self, matrix, m, n, row, col):
        if m > row >= 0 <= col < n and matrix[row][col] == '1':
            matrix[row][col] = '0'
            self.traverseIsland(matrix, m, n, row, col + 1)
            self.traverseIsland(matrix, m, n, row + 1, col)
            self.traverseIsland(matrix, m, n, row, col - 1)
            self.traverseIsland(matrix, m, n, row - 1, col)
            
# Official solution

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        totalIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    totalIslands += 1
                    self.visitIslandsDFS(grid, r, c)

        return totalIslands

    def visitIslandsDFS(self, grid, r, c):
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
            return

        if grid[r][c] == "0":
            return

        grid[r][c] = "0"

        self.visitIslandsDFS(grid, r, c + 1)
        self.visitIslandsDFS(grid, r + 1, c)
        self.visitIslandsDFS(grid, r - 1, c)
        self.visitIslandsDFS(grid, r, c - 1)
