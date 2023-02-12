class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in self.visited:
                    self.region = []
                    self.isBorderRegion = False
                    self.traverseRegion(board, m, n, i, j)
                    if not self.isBorderRegion:
                        for row, col in self.region:
                            board[row][col] = 'X'                    

    def traverseRegion(self, board, m, n, row, col):
        if row < 0 or row >= m or col < 0 or col >= n:
            self.isBorderRegion = True
            return
        if (row, col) in self.visited or board[row][col] == 'X':
            return
        self.visited.add((row, col))
        self.region.append((row, col))
        self.traverseRegion(board, m, n, row - 1, col)
        self.traverseRegion(board, m, n, row + 1, col)
        self.traverseRegion(board, m, n, row, col - 1)
        self.traverseRegion(board, m, n, row, col + 1)
        
# Official solution

class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        from itertools import product

        borders = list(product(range(self.ROWS), [0, self.COLS - 1])) + list(
                       product([0, self.ROWS - 1], range(self.COLS)))

        for row, col in borders:
            self.DFS(board, row, col)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # captured
                elif board[r][c] == "E":
                    board[r][c] = "O"  # escaped

    def DFS(self, board, row, col):
        if col < 0 or col >= self.COLS or row < 0 or row >= self.ROWS:
            return
            
        if board[row][col] != "O":
            return
            
        board[row][col] = "E"
        
        self.DFS(board, row, col + 1)
        self.DFS(board, row + 1, col)
        self.DFS(board, row, col - 1)
        self.DFS(board, row - 1, col)
