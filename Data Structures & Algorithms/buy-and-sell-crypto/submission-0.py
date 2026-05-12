class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay = 0
        sellDay = 0

        while sellDay < len(prices):
            current = prices[sellDay] - prices[buyDay]
            maxProfit = max(maxProfit,current)

            if prices[buyDay] > prices[sellDay]:
                buyDay += 1
            else:
                sellDay += 1
        return maxProfit

