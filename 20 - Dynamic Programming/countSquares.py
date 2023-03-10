class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j] <= matrix[i][j-1] and matrix[i][j] <= matrix[i-1][j] and matrix[i][j] <= matrix[i-1][j-1]:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
        
        return sum(matrix[i][j] for i in range(m) for j in range(n))
