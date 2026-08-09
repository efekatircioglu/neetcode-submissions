class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window vars length or two pointers
        # left=0 

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

        # for i in range(len(prices)-1):
        #     if prices[i]>prices[r]:
        #         r+=1
        #     elif prices[i]<prices[l]:
        #         l+=1
        #     currentProfit= prices[r]-prices[l]
        #     profit= max(profit,currentProfit)
        # return profit

        