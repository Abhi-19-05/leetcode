class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max1=0
        for i in range(len(accounts)):
            max1=max(sum(accounts[i]),max1)
        return max1
