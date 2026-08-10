class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of integers, and integer k
        # return: list of [k-most frequent element(s)]

        # Input: nums = [10,20,20,30,30,30], k = 2
        # Output: [20,30]

        # number int-> frequency int (default 0) hashmap
        counts = defaultdict(int)

        # {10:1, 20:2, 30:3}
        for num in nums:
            counts[num] +=1

        # sort that hashmap decreasing. sorting keys from their (keys,values)
        sorted_counts = sorted(counts.keys(), key=lambda num: counts[num], reverse=True)

        # return the k highest element
        return sorted_counts[:k]






























