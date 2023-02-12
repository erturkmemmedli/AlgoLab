class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        self.direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        row, col = click
        self.dfs(board, m, n, row, col)
        return board

    def dfs(self, board, m, n, row, col):
        if m > row >= 0 <= col < n:
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            elif board[row][col] == 'E':
                numMines = 0
                for r, c in self.direction:
                    if m > row + r >= 0 <= col + c < n and board[row + r][col + c] == 'M':
                        numMines += 1
                if numMines:
                    board[row][col] = str(numMines)
                else:
                    board[row][col] = 'B'
                    for r, c in self.direction:
                        self.dfs(board, m, n, row + r, col + c)
                        
# Official solution

class Solution:
    def updateBoard(self, board, click):
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        if board[i][j] == "M":
            board[i][j] = "X"
            
            return board

        self.dfs(board, i, j)
        
        return board

    def dfs(self, board, i, j):
        if board[i][j] != "E":
            return

        m, n = len(board), len(board[0])
        directions = [(-1, -1),(0, -1),(1, -1),(1, 0),
                      (1, 1),  (0, 1), (-1, 1),(-1, 0)]
        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]

            if 0 <= ni < m and 0 <= nj < n and 
               board[ni][nj] == "M":
                mine_count += 1

        if mine_count == 0:
            board[i][j] = "B"
        else:
            board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)
