class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given an array of length 
        # nums = [x, x+1, x+2 ... x+n-1]
        # nums have been rotated between (1 to n) times
        # time = O(log n) space = 0(1) => Binary Search
        #  [1,2,3,4,5,6]
        #  [3,4,5,6,1,2]
        #   l   m     r
        #         l m r
        # nums[] : l<m and not m<r:
        # discard left side of m: => l=m+1
        # if vise versa discard right side of m => r= m-1
        # l,m,r assign them normally, either at least nums[l]<nums[m] or nums[m]<nums[r]
        # if nums[l]<nums[m]:
        
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l] < nums [r]:
                res= min(res, nums[l])
                break

            m = l + (r-l)//2
            res = min (res,nums[m])

            if nums[m]>=nums[l]:
                if nums[m]>=nums[r]:
                    if nums[l]<nums[r]:
                        return nums[0]
                    else:
                        l=m+1
                else:
                    r=m-1
            else:
                r=m-1
                
        return res


