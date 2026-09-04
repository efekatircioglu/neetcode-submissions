class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            number=left+((right-left) //2)
            if nums[number] < target: 
                left=number+1
            elif nums[number] > target:
                 right=number-1
            else:
                return number

        return -1