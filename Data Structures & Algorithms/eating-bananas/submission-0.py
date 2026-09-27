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

        piles.sort()
        k=1
        low=1
        high=piles[-1]
        res=high

        while low <= high:
            mid = (high+low)//2
            
            total= sum(math.ceil(pile/mid) for pile in piles)
            if total <=h:
                res = mid
                high = res - 1
            else:
                low = mid + 1
                # start loop again
        return res
            