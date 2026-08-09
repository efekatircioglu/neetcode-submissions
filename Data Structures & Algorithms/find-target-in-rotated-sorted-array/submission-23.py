# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         l,r=0,len(nums)-1

#         while l<=r:
#             m = l + (r-l)//2

#             if nums[m] == target:
#                 return m

#             if nums[l]<=nums[m]:
#                 if nums[m]<target and target<nums[l]:
#                     l=m+1
#                 else:
#                     r=m-1
            
#             else:
#                 if nums[m]>target and target>nums[r]:
#                     r=m-1
#                 else:
#                     l=m+1
#         return -1
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            # Case 1: The left half is sorted
            if nums[l] <= nums[m]:
                # Check if target is in the sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1 # Correct action: search left
                else:
                    l = m + 1 # Correct action: search right
            
            # Case 2: The right half is sorted
            else:
                # Check if target is in the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1 # Correct action: search right
                else:
                    r = m - 1 # Correct action: search left
        return -1