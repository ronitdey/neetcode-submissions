class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay = 0
        sellDay = 0

        while sellDay < len(prices):
            maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])

            if prices[buyDay] > prices[sellDay]:
                buyDay += 1
            else:
                sellDay += 1
        return maxProfit

