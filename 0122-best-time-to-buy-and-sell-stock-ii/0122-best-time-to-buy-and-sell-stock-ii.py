class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
                
        return max_profit
        