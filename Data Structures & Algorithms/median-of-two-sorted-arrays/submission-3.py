class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # can have duplicated values



        # return the mid element of the merged arrays


        merged=[]
        i,j=0,0

        while i <len(nums1) and j<len(nums2):
            # compare nums1[i] vs nums2[j]
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        if i!=len(nums1):
            merged= merged+nums1[i:]
        else:
            merged= merged+nums2[j:]
            

        if len(merged)==0:
            return 0.0
        
        midIndex=len(merged)//2
        if len(merged)%2==1:
            return float(merged[midIndex])
        else:
            return float((merged[midIndex] + merged[midIndex-1])/2)

        