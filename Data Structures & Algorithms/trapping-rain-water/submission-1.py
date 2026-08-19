class Solution:
    def trap(self, height: List[int]) -> int:
        # water = left and right for that height has blocks
        # for a given height if that value is less than or equal to height of its left and right: res += min(left,right)-currentheight
        # or water stays in if there's water next to each other
        # min(prefix[i], suffix[i]) - height[i]
        if not height:
            return 0

        prefix = [0] * len(height)
        prefix[0]=height[0]
        suffix = [0] * len(height)
        suffix[-1]=height[-1]

        for i in range(1,len(height)):
            prefix[i] = max( prefix[i-1], height[i])


        for i in range(len(height)-2,-1,-1):
            suffix[i] += max(suffix[i+1] , height[i])
        
        result=0
        for i in range(len(height)):
            water_level =min(prefix[i], suffix[i]) 
            result += water_level - height[i]
        return result            
