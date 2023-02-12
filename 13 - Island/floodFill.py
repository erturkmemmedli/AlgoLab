class Solution:
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        referenceColor = image[sr][sc]
        self.dfs(image, m, n, referenceColor, sr, sc, color)
        return image

    def dfs(self, image, m, n, refColor, row, col, color):
        if (row < 0 or row >= m) or (col < 0 or col >= n) or image[row][col] == color or image[row][col] != refColor:
            return
        image[row][col] = color
        self.dfs(image, m, n, refColor, row - 1, col, color)
        self.dfs(image, m, n, refColor, row + 1, col, color)
        self.dfs(image, m, n, refColor, row, col - 1, color)
        self.dfs(image, m, n, refColor, row, col + 1, color)
        
# Official solution

class Solution:
    def floodFill(self, image, sr, sc, color):
        startingPixel = image[sr][sc]

        if image[sr][sc] != color:
            self.fillColor(image, sr, sc, color, startingPixel)

        return image

    def fillColor(self, image, i, j, color, startingPixel):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return

        if image[i][j] != startingPixel:
            return

        image[i][j] = color

        self.fillColor(image, i, j + 1, color, startingPixel)
        self.fillColor(image, i + 1, j, color, startingPixel)
        self.fillColor(image, i, j - 1, color, startingPixel)
        self.fillColor(image, i - 1, j, color, startingPixel)
