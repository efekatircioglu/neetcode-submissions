class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        heapq.heapify(nums)
        print(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        print(nums)
        return nums[0]