class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0


        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2





"""
# we go to the house that has highest value, and we cannot go its adjacents



# Base Cases
if len(nums) == 0: return 0
if len(nums) == 1: return nums[0]

# Calculations

rob = max(arr[0]+rob[2:n], rob[1:n])






"""
        