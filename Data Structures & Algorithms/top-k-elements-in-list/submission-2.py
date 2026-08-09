class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of integers, and integer k
        # return: list of [k-most frequent element(s)]

        
        counts = defaultdict(int)
        # num(int) -> freq(int)
        for num in nums:
            counts[num] +=1

        # sorting counts 
        sorted_nums = sorted(counts.keys(), key=lambda n: counts[n], reverse=True)
        return sorted_nums[:k]
        


        '''
        for num in nums:

        '''
        
