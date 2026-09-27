class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target value exist, return nums[target]. if not return -1
        l,r=0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                    return mid
            # left sorted array
            if nums[l] <= nums[mid]: 
                if nums[mid]<target or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            # right sorted array
            if nums[mid]<=nums[r]:
                if nums[mid]>target or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1    
               
        return -1
            
        