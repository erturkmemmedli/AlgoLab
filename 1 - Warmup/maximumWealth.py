class Solution:
    def maximumWealth(self, accounts):
        rich = 0
        for account in accounts:
            rich = max(rich, sum(account))
        return rich
		
# Official solution given

class Solution:
    def maximumWealth(self, accounts):
        maxWealth = 0
        for account in accounts:
            wealth = sum(account)
            maxWealth = max(maxWealth, wealth)
        return maxWealth
