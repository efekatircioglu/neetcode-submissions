class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for each bar, find nearest smaller bar to LEFT
        stack=[]
        leftMost=[-1] * len(heights)
        for i in range(len(heights)):
            #pop bars not smaller than current
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            # if stack not empty, top of it is the nearest smaller bar to left, add it
            if stack:
                leftMost[i]=stack[-1]
            stack.append(i)

        # for each bar, find nearest smaller bar to RIGHT
        stack=[]
        rightMost=[len(heights)] * len(heights)
        for i in range(len(heights)-1,-1,-1):
            #pop bars not smaller than current
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            # if stack not empty, top of it is the nearest smaller bar to right, add it
            if stack:
                rightMost[i]=stack[-1]
            stack.append(i)

        # CALCULATE AREA
        maxArea=0
        for i in range(len(heights)):
            leftMost[i] +=1
            rightMost[i] -=1
            maxArea = max(maxArea,heights[i]*(rightMost[i]-leftMost[i]+1))
        return maxArea