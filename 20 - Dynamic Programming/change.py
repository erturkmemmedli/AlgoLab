class Solution:
    def change(self, amount, coins):
        self.memo = {}
        return self.dp(amount, coins, 0)

    def dp(self, amount, coins, index):
        if amount == 0:
            return 1

        if amount < 0 or index == len(coins):
            return 0

        if (amount, index) in self.memo:
            return self.memo[(amount, index)]

        self.memo[(amount, index)] = self.dp(amount - coins[index], coins, index) + self.dp(amount, coins, index + 1)
        return self.memo[(amount, index)]
        
# Official solution

class Solution:
    def change(self, amount, coins):
        memo = {}
        return self.helper(amount, coins, 0, memo)

    def helper(self, amount, coins, currentIndex, memo):
        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if currentIndex >= len(coins):
            return 0

        key = f"{currentIndex}#{amount}"

        if key in memo:
            return memo[key]
        
        ways = self.helper(amount - coins[currentIndex], coins, currentIndex, memo) + \
               self.helper(amount, coins, currentIndex + 1, memo)

        memo[key] = ways
        
        return ways
