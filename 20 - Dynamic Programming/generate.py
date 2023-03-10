class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(numRows - 1):
            dp = [1]
            for i in range(len(pascal[-1]) - 1):
                dp.append(pascal[-1][i] + pascal[-1][i + 1])
            dp.append(1)
            pascal.append(dp)
        return pascal
