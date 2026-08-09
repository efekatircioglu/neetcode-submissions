class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax =  globalmin = nums[0]
        curmax, curmin = 0,0
        total = 0

        for n in nums:
            curmax = max(n, curmax + n)
            curmin = min(n, curmin + n)
            total += n
            

            globalmax = max(curmax, globalmax)
            globalmin = min(curmin, globalmin)

        if globalmax > 0 :
            return max(globalmax, total - globalmin) 
        else:
            return globalmax
