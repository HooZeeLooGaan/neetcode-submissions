class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            res = max(res, (max(prices[i:]) - prices[i]))
        return res