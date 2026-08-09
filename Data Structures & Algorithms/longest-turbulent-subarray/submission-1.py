class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r=0,1
        res=1
        prev = ""

        while r<len(arr):
            # left > right
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r +=1
                prev = ">"
            # left < right
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res,r-l+1)
                r+=1
                prev = "<"
            # left = right
            else:
                r = r+1 if arr[r] == arr[r-1] else r
                l=r-1
                prev = ""
        return res
        