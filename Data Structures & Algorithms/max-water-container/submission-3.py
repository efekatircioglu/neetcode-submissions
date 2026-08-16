class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate curArea, maxArea
        l,r=0,len(heights)-1
        # if l+=1 or r-=1 makes curArea>maxArea: maxArea=curArea
        maxArea=0

        while l<r:
            curArea = (r-l) * min(heights[l],heights[r])
            if (heights[l] > heights[r]):
                r -=1
            elif (heights[l] <= heights[r]):
                l +=1
            maxArea = max(maxArea,curArea)
        return maxArea
        