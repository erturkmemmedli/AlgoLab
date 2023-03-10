class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        for i in range(rowIndex):
            dp = [1]
            for i in range(len(pascal) - 1):
                dp.append(pascal[i] + pascal[i + 1])
            dp.append(1)
            pascal = dp[:]
        return pascal
