class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(arr):
            if len(arr) ==1: return arr[0]
            prev, cur = arr[0], max(arr[0],arr[1])

            for i in range(2,len(arr)):
                prev, cur = cur, max(prev + arr[i], cur)
            return cur
        return max(rob1(nums[1:]), rob1(nums[:len(nums)-1]))


        