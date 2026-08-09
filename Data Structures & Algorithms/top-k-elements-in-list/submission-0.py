class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToOccur= {}
        freq = [[]for i in range(len(nums)+1)]

        for num in nums:
            numToOccur[num] = 1 + numToOccur.get(num,0)
        
        for num,occur in numToOccur.items():
            # add it to array
            freq[occur].append(num)

        res= []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res