class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums={}
        for i in range(len(nums)):
            if nums[i] in seenNums:
                return True
            seenNums[nums[i]]=nums[i]
            
        return False