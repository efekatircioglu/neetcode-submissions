class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # can have duplicated values



        # return the mid element of the merged arrays


        merged = nums1 + nums2
        merged.sort()

        if len(merged)==0:
            return 0.0
        if len(merged)%2==1:
            midIndex=len(merged)//2
            return float(merged[midIndex])
        else:
            midIndex=len(merged)//2
            midIndex2=midIndex-1
            return float((merged[midIndex] + merged[midIndex2])/2)

        