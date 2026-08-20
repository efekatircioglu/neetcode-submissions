class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        maxProfit=0

        for i in range(len(prices)):
            profit = prices[i]-low
            if prices[i] < low:
                low=prices[i]
            maxProfit = max(maxProfit,profit)
        return maxProfit
