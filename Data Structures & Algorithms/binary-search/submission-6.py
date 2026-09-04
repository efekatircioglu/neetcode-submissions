class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            number=(right+left) //2
            if nums[number]==target:
                return number
            elif nums[number] < target: 
                left=number+1
            else:
                 right=number-1

        return -1

