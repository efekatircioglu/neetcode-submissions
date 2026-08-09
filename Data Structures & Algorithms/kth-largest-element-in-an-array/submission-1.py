class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time= O(N) space=O(1)
        heapq.heapify(nums) 
        # time O(N-K)logN space=O(1)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]