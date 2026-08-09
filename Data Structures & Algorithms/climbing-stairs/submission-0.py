class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1

        prev, cur = 0, 1

        for _ in range (n):
            prev, cur = cur, prev+cur
        return cur        