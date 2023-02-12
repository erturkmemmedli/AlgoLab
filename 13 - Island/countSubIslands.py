class Solution:
    def countSubIslands(self, grid1, grid2):
        m = len(grid1)
        n = len(grid1[0])
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.included = True
                    self.visitIsland(grid1, grid2, m, n, i, j)
                    if self.included:
                        numIslands += 1
        return numIslands

    def visitIsland(self, grid1, grid2, m, n, row, col):
        if m > row >= 0 <= col < n and grid2[row][col]:
            if grid1[row][col] == 0:
                self.included = False
            grid2[row][col] = 0
            self.visitIsland(grid1, grid2, m, n, row - 1, col)
            self.visitIsland(grid1, grid2, m, n, row + 1, col)
            self.visitIsland(grid1, grid2, m, n, row, col - 1)
            self.visitIsland(grid1, grid2, m, n, row, col + 1)
            
# Official solution

class Solution:
    def countSubIslands(self, grid1, grid2):
        count = 0
        n = len(grid2)
        m = len(grid2[0])

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    grid2[i][j] = 2

                    if self.isIsland(i, j, n, m):
                        count += 1

        return count

    def isIsland(self, i, j, n, m):
        flag = True

        if grid1[i][j] != 1:
            flag = False

        if i - 1 >= 0 and grid2[i - 1][j] == 1:
            grid2[i - 1][j] = 2

            flag = self.isIsland(i - 1, j, n, m) and 
                   flag and grid1[i - 1][j]

        if i + 1 < n and grid2[i + 1][j] == 1:
            grid2[i + 1][j] = 2

            flag = self.isIsland(i + 1, j, n, m) and 
                   flag and grid1[i + 1][j]

        if j - 1 >= 0 and grid2[i][j - 1] == 1:
            grid2[i][j - 1] = 2

            flag = self.isIsland(i, j - 1, n, m) and 
                   flag and grid1[i][j - 1]

        if j + 1 < m and grid2[i][j + 1] == 1:
            grid2[i][j + 1] = 2

            flag = self.isIsland(i, j + 1, n, m) and 
                   flag and grid1[i][j + 1]

        return flag
