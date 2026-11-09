class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 1
        while i < len(prices):
            single_day_transact = prices[i] - prices[i - 1]
            if single_day_transact > 0:
                max_profit += single_day_transact
            i += 1
            
        return max_profit