class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay = 0
        sellDay = 1

        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                current = prices[sellDay] - prices[buyDay]
                maxProfit = max(maxProfit,current)
            else:
                buyDay = sellDay
        
            sellDay += 1
        return maxProfit

