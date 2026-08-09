class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # F: -9 S: -8    (9 - 8=1) (-9 - -8 = -1) (-8 --9) sec - f
            if second > first:
                heapq.heappush(stones, first-second)
            
        stones.append(0)
        print (stones)
        return abs(stones[0])
        