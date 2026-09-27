class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res=nums[0]

        while l<=r:
            # not rotated
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            # rotated
            mid = (r+l)//2
            res=min(res,nums[mid])
            if nums[l] <= nums[mid]:
                # min in mid->right
                l=mid+1
            else:
                # min in left->mid
                r=mid-1
        return res
            