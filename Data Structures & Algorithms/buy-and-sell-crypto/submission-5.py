class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,profit=0,1,0

        while r< len(prices):
            currentProfit=0
            if prices[l]<prices[r]:
                currentProfit= prices[r]-prices[l]
            else:
                l=r
            r+=1
            profit= max(profit,currentProfit)
        return profit


        