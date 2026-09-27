# from collections import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort the algorithm in increasing order
        # piles = [1,2,3,4]
        # k =1 -> 10   
        # k=2 -> 6
        # k = 3 -> 5
        # k = 4 -> 4

        # start from beginning: at each step divide piles[i] / k (round to up) = hours_needed_to_eat_pile
        # and total += hours_needed_to_eat_pile
        # at the end if total > h: continue. else: return k

        k=1
        low=1
        high=max(piles)
        res=high

        while low <= high:
            k = (high+low)//2
            total= sum(math.ceil(k) for pile in piles)
            if total <=h:
                res = k
                high = res - 1
            else:
                low = k + 1
        return res
            